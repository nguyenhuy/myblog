from django.conf.urls import patterns
from MyBlogApp.rest_views import rest_add_blog
from MyBlogApp.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', show_all_blogs),
    (r'^myblog/$', show_all_blogs),
    (r'^editblog/(?P<blog_id>\d+)$', edit_blog),
    (r'^myblog/(?P<blog_id>\d+)$', show_blog),
    (r'^addblog/$', add_blog),
    (r'^deleteblog/(?P<blog_id>\d+)$', delete_blog),
    (r'^reset_session/$', reset_session),
    (r'^createuser/$', register),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    (r'^api/v1/blog/add$', rest_add_blog)
    # url(r'^$', 'MyBlog.views.home', name='home'),
    # url(r'^MyBlog/', include('MyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
