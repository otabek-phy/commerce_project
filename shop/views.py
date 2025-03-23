from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from shop.models import Category, Product, Customer
from django.contrib.auth import login
from .forms import RegisterForm


def index(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        context = {'category': category, 'products': products}
        return render(request, 'shop/product-list.html', context)
    context = {'categories': categories, 'products': products}
    return render(request, 'shop/index.html', context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product': product}
    return render(request, 'shop/product-detail.html', context)


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/product-detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'


class IndexView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')
        context['categories'] = Category.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            context['category'] = category
            context['products'] = Product.objects.filter(category=category)
            self.template_name = 'shop/product-list.html'
        else:
            context['products'] = Product.objects.all()
        return context


class CustomerListView(ListView):
    model = Customer
    template_name = 'shop/customers.html'
    context_object_name = 'customers'


class RegisterView(View):
    template_name = "shop/register.html"

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        return render(request, self.template_name, {"form": form})
