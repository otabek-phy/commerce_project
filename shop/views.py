from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from shop.models import Category, Product, Customer
from django.contrib.auth import login
from .forms import RegisterForm



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





class RegisterView(View):
    template_name = "shop/register.html"

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Foydalanuvchini avtomatik login qilish
            return redirect("shop:home")  # Asosiy sahifaga yo'naltirish
        return render(request, self.template_name, {"form": form})
