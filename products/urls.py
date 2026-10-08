from django.urls import path

from .views import (dashboard,product_list,product_create,product_edit,product_detail,product_delete,user_logout)


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('products/', product_list, name='product_list'),
    path('products/add/', product_create, name='product_create'),
    path('products/<int:pk>/edit/',product_edit, name='product_edit'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('products/<int:pk>/delete/', product_delete, name='product_delete'),
    path('logout/', user_logout, name='logout'),
]