from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_accessories, name='accessories'),
    path('<int:accessories_id>/', views.accessory_detail, name='accessory_detail'),
    path('add/', views.add_accessory, name='add_accessory'),
    path('edit/<int:accessories_id>/', views.edit_accessory, name='edit_accessory'),
    path('delete/<int:accessories_id>/', views.delete_accessory, name='delete_accessory'),
]
