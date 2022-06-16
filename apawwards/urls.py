from django.contrib import admin
from django.urls import path, include
from . import views
from awwardsprj import settings
from django.conf.urls.static import  static






urlpatterns=[
    path('',views.home,name='home'),
    path('project/<int:project_id>/',views.projects,name='projects'),
    path('profile<username>/', views.profile, name='profile'),
    path('uploads/',views.post_site,name='post_site'),
    path('api/profiles/', views.ProfileList.as_view(),name='profile_list'),
    path('api/projects/', views.ProjectsList.as_view(),name='projects_list'),
    path('search/', views.search_results, name='search_results'),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)