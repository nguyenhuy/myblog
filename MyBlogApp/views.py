# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from MyBlogApp.models import Blog


def show_all_blogs(request):
    init_session_if_needed(request)
    blogs = Blog.objects.all()
    if len(blogs) == 0:
        messages.info(request, 'No blog post for now.')
    return render_to_response('blogs.html',
                              {'blogs': blogs},
                              context_instance=RequestContext(request))


def edit_blog(request, blog_id):
    init_session_if_needed(request)
    if Blog.exists(blog_id):
        blog = Blog.objects.get(id=blog_id)
        if request.method == "POST" \
                and request.POST.has_key('content') \
                and request.session.has_key('edited_version'):
            edited_version = int(request.session['edited_version'])
            user_content = request.POST['content'].strip()
            if edited_version == blog.version:
                # The blog post has not been changed, it can be updated now.
                blog.content = user_content
                blog.version += 1
                blog.save()

                request.session['edit_counter'] += 1
                return HttpResponseRedirect('/myblog')
            else:
                # The article was changed by someone else, ask user to
                # resolve conflicts.
                request.session['edited_version'] = blog.version
                return render_to_response("resolve_conflicts.html",
                                          {
                                              'id': blog.id,
                                              'title': blog.title,
                                              'current_content': blog.content,
                                              'user_content': user_content
                                          },
                                          context_instance=RequestContext(
                                              request))
        else:
            request.session['edited_version'] = blog.version
            return render_to_response("edit_blog.html",
                                      {
                                          'title': blog.title,
                                          'id': blog.id,
                                          'content': blog.content
                                      },
                                      context_instance=RequestContext(request))
    else:
        return render_to_response("no_blog.html",
                                  {"id": blog_id},
                                  context_instance=RequestContext(request))


def show_blog(request, blog_id):
    init_session_if_needed(request)
    if Blog.exists(blog_id):
        request.session['visit_counter'] += 1
        blog = Blog.objects.get(id=blog_id)
        return render_to_response("blog.html",
                                  {'title': blog.title,
                                   'content': blog.content},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response("no_blog.html",
                                  {'id': blog_id},
                                  context_instance=RequestContext(request))


def add_blog(request):
    init_session_if_needed(request)
    if request.method == "POST" \
            and request.POST.has_key('title') \
            and len(request.POST['title'].strip()) > 0 \
            and request.POST.has_key('content'):
        blog = Blog(title=request.POST['title'].strip(),
                    content=request.POST['content'].strip(),
                    time_stamp=datetime.now())
        blog.save()

        request.session['create_counter'] += 1
        messages.success(request,
                         'New blog with title ' + blog.title + ' has been added.')
        return HttpResponseRedirect('/myblog')
    else:
        return render_to_response("add_blog.html",
                                  context_instance=RequestContext(request))


def delete_blog(request, blog_id):
    init_session_if_needed(request)
    if Blog.exists(blog_id):
        blog = Blog.objects.get(id=blog_id)
        blog.delete()

        request.session['delete_counter'] += 1
        return HttpResponseRedirect('/myblog')
    else:
        return render_to_response("no_blog.html",
                                  {'id': blog_id},
                                  context_instance=RequestContext(request))


def init_session(request):
    request.session['start_date'] = datetime.now()
    request.session['visit_counter'] = 0
    request.session['edit_counter'] = 0
    request.session['create_counter'] = 0
    request.session['delete_counter'] = 0


def init_session_if_needed(request):
    if not request.session or not request.session.has_key('start_date'):
        init_session(request)


def reset_session(request):
    init_session(request)
    return HttpResponseRedirect('/myblog/')