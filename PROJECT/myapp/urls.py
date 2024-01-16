from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('clients/',views.clients),
    path('about/',views.about),
    path('contact/',views.contact),
    path('projects/',views.projects),
    path('services/',views.services),
    path('estimate/',views.estimate),
]