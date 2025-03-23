from django.contrib import admin
from django.urls import path
from shop.views import IndexView, ProductDetail, CustomerListView, RegisterView
from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products_list/<slug:category_slug>/', views.IndexView.as_view(), name='products_list_by_category'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('register/',views.RegisterView.as_view(),name='register'),
]
