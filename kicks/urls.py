"""
Kicks App URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_kicks, name='kicks'),
    path('<int:kicks_id>/', views.kicks_detail, name='kicks_detail'),
    path('add/', views.add_kicks, name='add_kicks'),
    path('edit/<int:kicks_id>/', views.edit_kicks, name='edit_kicks'),
    path('delete/<int:kicks_id>/', views.delete_kicks, name='delete_kicks'),
]
