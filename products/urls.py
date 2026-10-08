from django.urls import path
from .views import dashboard, product_list

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('products/', product_list, name='product_list'),
]