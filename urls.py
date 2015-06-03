from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),
    url(r'^context/id/[0-9]+\.html$','app.views.context',name='context'),
    url(r'^index/id/[0-9]+/sequence/[1-2]\.html$','app.views.index', name='index'),
    url(r'^login\.html$','app.views.login',name='login'),
    url(r'^register\.html$','app.views.register',name='register'),
    url(r'^share\.html$','app.views.share',name='share'),
    url(r'^update\.html$','app.views.update',name='update'),
    url(r'^updateIn\.html$','app.views.updateIn',name='updateIn'),
    url(r'^search\.html','app.views.search',name='search'),
    url(r'^admin/login\.html','admin.views.login',name='admin.login'),
    url(r'^admin/loginIn\.html$','admin.views.loginIn',name='admin.loginIn'),
    url(r'^admin/index\.html$','admin.views.index',name='admin.index'),
    url(r'^admin/getBook\.html$','admin.views.getBook',name='admin.book')
)
