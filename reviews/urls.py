from django.contrib import admin
from django.urls import path, include
from reviews import views

urlpatterns = [
    path('', views.reviewsHome, name='reviewsHome'),
    
    path('<str:slug>', views.reviewsProduct, name='reviewsProduct'),
]
