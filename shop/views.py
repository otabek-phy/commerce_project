from django.shortcuts import render, get_object_or_404

from shop.models import Category, Product, Customer
from django.core.paginator import Paginator



# Create your views here.


def index(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()

    paginator = Paginator(products, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    if category_id:
        products = Product.objects.filter(category_id=category_id)
        return render(request, 'shop/product-list.html', {'products': products})

    context = {
        'categories': categories,
        'page_obj': page_obj,
        'products': products
    }
    return render(request, 'shop/index.html', context)




def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'shop/customers.html', {'customers': customers})
