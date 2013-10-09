# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from MyBlogApp.models import Blog


def show_all_blogs(request):
    blogs = Blog.objects.all()
    if len(blogs) == 0:
        messages.info(request, 'No blog post for now.')
    return render_to_response('blogs.html',
                              {'blogs': blogs},
                              context_instance=RequestContext(request))


def edit_blog(request, blog_id):
    if Blog.exists(blog_id):
        blog = Blog.objects.get(id=blog_id)
        if request.method == "POST" and request.POST.has_key('content'):
            blog.content = request.POST['content'].strip()
            blog.save()
            return HttpResponseRedirect('/myblog')
        else:
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
    if Blog.exists(blog_id):
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
    if request.method == "POST" \
        and request.POST.has_key('title') \
        and len(request.POST['title'].strip()) > 0 \
        and request.POST.has_key('content'):

        blog = Blog(title=request.POST['title'].strip(),
                    content=request.POST['content'].strip(),
                    time_stamp=datetime.now())
        blog.save()
        messages.success(request,
                         'New blog with title ' + blog.title + ' has been added.')
        return HttpResponseRedirect('/myblog')
    else:
        return render_to_response("add_blog.html",
                                  context_instance=RequestContext(request))


def delete_blog(request, blog_id):
    if Blog.exists(blog_id):
        blog = Blog.objects.get(id=blog_id)
        blog.delete()
        return HttpResponseRedirect('/myblog')
    else:
        return render_to_response("no_blog.html",
                                  {'id': blog_id},
                                  context_instance=RequestContext(request))