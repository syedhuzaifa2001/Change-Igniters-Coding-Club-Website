from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact-home'),
    # path('contact/', views.contact, name='contact'),
]