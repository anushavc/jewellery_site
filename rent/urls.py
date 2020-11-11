from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main,name="main"),
    path('cart/', views.cart,name="main"),
    path('checkout/', views.checkout,name="main"),
    path('rent/', views.renting,name="main"),
]
