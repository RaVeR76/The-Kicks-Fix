from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_kicks, name='kicks'),
    path('<int:kicks_id>/', views.kicks_detail, name='kicks_detail'),
    path('add/', views.add_kicks, name='add_kicks'),
]
