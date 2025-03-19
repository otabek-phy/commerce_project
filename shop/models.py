from decimal import Decimal

from django.db import models


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category/images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def discounted_price(self):
        if self.discount > 0:
            discount_price = self.price * Decimal(1 - self.discount / 100)
            return Decimal(f'{discount_price}').quantize(Decimal('0.00'))

        return Decimal(f'{self.price}').quantize(Decimal('0.00'))

    @property
    def get_absolute_url(self):
        primary_image = self.images.all().order_by('my_order')[0]
        print(primary_image)
        return primary_image.image.url

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='product/images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', null=True, blank=True)

    my_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product.name} {self.image.url}'

    class Meta:
        verbose_name_plural = "Images"




from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

