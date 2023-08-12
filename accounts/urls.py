from django.urls import path
from . import views
from . views import PublicProfile

urlpatterns = [
    path('register/', views.register, name='account-register'),
    path('myprofile/', views.profile, name='account-profile'),
    path('myprofile/edit', views.editprofile, name='account-editprofile'),
    path('myprofile/edit/profile_picture', views.editprofilepicture, name='account-editprofilepicture'),
    path('profiles/<str:slug>/', PublicProfile.as_view(), name='account-publicprofile'),
    path('login/', views.login, name='account-login'),
    path('', views.logout, name='account-logout'),
    path('join-community/', views.joinCommunity, name='account-joincommunity'),
]