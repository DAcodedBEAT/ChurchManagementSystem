from django.conf.urls import patterns, url
from Accounting import views

from django.shortcuts import redirect


urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^input/$', views.input_income, name='input_income'),
    url(r'^edit/$', views.edit_income, name='edit_income'),
    url(r'^edit/(?P<event_id>[^/]+)/$', views.edit_specific_income, name='edit_specific_income'),
    url(r'^delete/$', views.delete_income, name='delete_income'),
    url(r'^delete/(?P<event_id>[^/]+)/$', views.delete_specific_income, name='delete_specific_income'),


    url(r'^upload_income/$', views.upload_income, name='upload_income'),
    url(r'^download_income/$', views.download_income, name='download_income'),
    url(r'^download_income/(?P<sheet_name>[^/]+)/$', views.download_sheet_income, name='download_sheet_income'),
    url(r'^download_all_incomes/$', views.download_all_incomes, name='download_all_incomes'),

    url(r'^pledge_acct/(?P<pledge_id>[^/]+)/$', views.view_pledge, name='view_pledge'),
    url(r'^pledge_acct/my/$', views.my_pledge, name='my_pledge'),
)
