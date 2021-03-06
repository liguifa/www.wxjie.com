from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),
    url(r'^context_id_[0-9]?.html$','app.views.context',name='context'),
    url(r'^index_id_[0-9]?.html$','app.views.index', name='index'),
    url(r'^login.html$','app.views.login',name='login'),
    url(r'^register.html$','app.views.register',name='register'),
    url(r'^share.html$','app.views.share',name='share'),
    url(r'^update.html$','app.views.update',name='update'),
    url(r'^updateIn.html$','app.views.updateIn',name='updateIn')
)
