from django.contrib import admin

from shop.models import Category, Product, Images, Attribute, AttributeValue, ProductAttribute, Customer

# Register your models here.


# admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Customer)
class Admin(admin.ModelAdmin):


 admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {"slug": ("title",)}
