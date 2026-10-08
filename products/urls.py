from django.urls import path

from .views import (dashboard,product_list,product_create,product_edit,)


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('products/', product_list, name='product_list'),
    path('products/add/', product_create, name='product_create'),
    path('products/<int:pk>/edit/',product_edit, name='product_edit'),
]