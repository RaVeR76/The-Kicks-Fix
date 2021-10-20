from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_kicks, name='kicks')
]
