""" Profiles App URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/', views.order_history, name='order_history'),
    path('previous_orders/<order_number>',
         views.previous_orders, name='previous_orders'),
]
