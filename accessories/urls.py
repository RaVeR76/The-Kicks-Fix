from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_accessories, name='accessories'),
    path('<accessories_id>', views.accessory_detail, name='accessory_detail'),
]
