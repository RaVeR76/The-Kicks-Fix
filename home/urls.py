"""
Home App URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact_us, name='contact_us'),
    path('club/', views.kicks_club, name='kicks_club'),
]
