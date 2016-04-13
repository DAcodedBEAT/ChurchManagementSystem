from django.conf.urls import patterns, url
from Accounting import views

from django.shortcuts import redirect


urlpatterns = patterns('Accounting.views',
    url(r'^$', 'dashboard', name='dashboard'),
    url(r'^input/$', 'input_income', name='input_income'),
    url(r'^edit/$', 'edit_income', name='edit_income'),
    url(r'^edit/(?P<event_id>[^/]+)/$', 'edit_specific_income', name='edit_specific_income'),
    url(r'^delete/$', 'delete_income', name='delete_income'),
    url(r'^delete/(?P<event_id>[^/]+)/$', 'delete_specific_income', name='delete_specific_income'),


    url(r'^upload_income/$', 'upload_income', name='upload_income'),
    url(r'^download_income/$', 'download_income', name='download_income'),
    url(r'^download_income/(?P<sheet_name>[^/]+)/$', 'download_sheet_income', name='download_sheet_income'),
    url(r'^download_all_incomes/$', 'download_all_incomes', name='download_all_incomes'),

    url(r'^pledge_acct/(?P<pledge_id>[^/]+)/$', 'view_pledge', name='view_pledge'),
    url(r'^pledge_acct/my/$', 'my_pledge', name='my_pledge'),
)
