from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('galleryselected/<str:Gallery_slug>', views.galleryselected, name='gallery-selected'),
]