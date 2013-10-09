from django.conf.urls import patterns
from MyBlogApp.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^myblog/$', show_all_blogs),
    (r'^editblog/(?P<blog_id>\d+)$', edit_blog),
    (r'^myblog/(?P<blog_id>\d+)$', show_blog),
    (r'^addblog/$', add_blog),
    (r'^deleteblog/(?P<blog_id>\d+)$', delete_blog)
    # url(r'^$', 'MyBlog.views.home', name='home'),
    # url(r'^MyBlog/', include('MyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
