from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blogs-home'),
    path('selected/<int:id>', views.selected, name='blogs-selected'),
]