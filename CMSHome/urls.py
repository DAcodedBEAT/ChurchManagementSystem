from django.conf.urls import patterns, url

urlpatterns = patterns('CMSHome.views',
    url(r'^$', 'home', name='home'),
)