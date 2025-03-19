from django.contrib import admin

from shop.models import Category, Images, Product, Customer

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Customer)
