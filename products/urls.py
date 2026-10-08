from django.urls import path

from .views import (dashboard,product_list,product_create,)


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('products/', product_list, name='product_list'),
    path('products/add/', product_create, name='product_create'),
]