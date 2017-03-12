from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^companyform/$', views.CreateCompanyProfile, name='companyform'),
    url(r'^userform/$', views.CreateUserProfile, name='userform'),
    url(r'^member/(?P<pk>\d+)/$', views.UserDetailView.as_view(), name='member'),	
    url(r'^company/(?P<pk>\d+)/$', views.CompanyDetailView.as_view(), name='company'),	
    url(r'^companies/', views.CompanyListView.as_view(), name='companies'),	
    url(r'^members/', views.UserListView.as_view(), name='members'),	
    url(r'^createcompany/', views.create_company, name='create_company'),
    url(r'^createuser/', views.create_member, name='createuser')
]