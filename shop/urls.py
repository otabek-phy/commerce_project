from django.contrib import admin
from django.urls import path
from shop.views import IndexView, ProductDetailView, CustomerListView, RegisterView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products_list/<int:pk>/', IndexView.as_view(), name='products_list_by_category'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('customers/', CustomerListView.as_view(), name='customers_list'),
    path('register/',RegisterView.as_view(),name='register'),
]
