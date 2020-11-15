from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.main,name="main"),
    path('rent/', views.rent,name="rent"),
 
]
