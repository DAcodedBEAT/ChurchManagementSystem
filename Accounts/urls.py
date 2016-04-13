from django.conf.urls import patterns, url
from Accounts import views

from django.shortcuts import redirect


urlpatterns = patterns('Accounts.views',
    # url(r'^$', lambda x: redirect(views.my_account),
    url(r'^login/$', 'user_login', name='login'),
    url(r'^logout/$', 'user_logout', name='logout'),
    url(r'^register/$', 'user_register', name='register'),
    #url(r'^my_account/$', 'my_account', name='my_account'),
    #url(r'^users/(?P<u_id>[^/]+)/$', 'view_user', name='view_user'),
    #url(r'^create_profile/$', 'create_profile', name='create_profile'),
    #url(r'^edit_profile/$', 'edit_profile', name='edit_profile'),
    #url(r'^deactivate_user/$', 'deactivate_user', name='deactivate_user'),
    #url(r'^delete_user/$', 'delete_user', name='delete_user'),
)
