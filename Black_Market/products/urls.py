from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/', views.products),
    path('product/<int:id_prod>/', views.product),
    path('seller/<int:id_seller>/', views.seller),
]
