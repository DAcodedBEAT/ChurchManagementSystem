from django.conf.urls import patterns, url
from Accounts import views

from django.shortcuts import redirect


urlpatterns = patterns('',
    # url(r'^$', lambda x: redirect(views.my_account),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.user_register, name='register'),
    #url(r'^my_account/$', views.my_account, name='my_account'),
    #url(r'^users/(?P<u_id>[^/]+)/$', views.view_user, name='view_user'),
    #url(r'^create_profile/$', views.create_profile, name='create_profile'),
    #url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    #url(r'^deactivate_user/$', views.deactivate_user, name='deactivate_user'),
    #url(r'^delete_user/$', views.delete_user, name='delete_user'),
)
