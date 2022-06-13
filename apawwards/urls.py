from django.urls import path, include
from . import views






urlpatterns=[
    path('',views.home,name='home'),
    path('projects/(\d+)',views.projects,name='projects'),
    path('profile/(?P<username>\w+)', views.profile, name='profile'),
    path('uploads/',views.post_site,name='post_site'),
    path('api/profiles/', views.ProfileList.as_view(),name='profile_list'),
    path('api/projects/', views.ProjectsList.as_view(),name='projects_list'),
    path('search/', views.search_results, name='search_results'),
    ]