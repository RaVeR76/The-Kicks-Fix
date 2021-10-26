from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_kicks, name='kicks'),
    path('<kicks_id>', views.kicks_detail, name='kicks_detail'),
]
