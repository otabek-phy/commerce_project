from django.contrib import admin
from django.urls import path, include

from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/<int:category_id>', views.index, name='product_list'),
    path('customer_list/<int:id>', views.customer_list, name='customer_list'),
]