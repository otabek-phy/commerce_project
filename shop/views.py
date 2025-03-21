from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from shop.models import Category, Product, Customer



class IndexView(View):
    def get(self, request, category_id=None):
        categories = Category.objects.all()
        products = Product.objects.all()

        if category_id:
            products = products.filter(category=category_id)
            return render(request, 'shop/product-list.html', {'products': products})

        context = {'categories': categories, 'products': products}
        return render(request, 'shop/index.html', context)



class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product-detail.html'
    context_object_name = 'product'



class CustomerListView(ListView):
    model = Customer
    template_name = 'shop/customers.html'
    context_object_name = 'customers'
