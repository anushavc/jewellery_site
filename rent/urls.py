from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main,name="main"),
    path('cart/', views.cart,name="main"),
    path('checkout/', views.checkout,name="main"),
    path('rent/', views.renting,name="main"),
    
    path('login/', views.login,name="login"),
    path('register/', views.register,name="register"),
    path('logout/', views.logout,name="logout"),
    
    path('update_item/', views.updateItem,name="main"),
]
