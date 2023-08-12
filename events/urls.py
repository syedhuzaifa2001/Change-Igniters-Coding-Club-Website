from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='events-home'),
    path('leaderboard/', views.leaderboard, name='events-leaderboard'),
    path('apply/', views.apply, name='events-apply'),

]