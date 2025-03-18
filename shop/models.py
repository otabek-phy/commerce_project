from tkinter.tix import IMAGE

from django.db import models
from decimal import Decimal

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='category/images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'



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
            self.price = self.price * Decimal(1 - self.discount / 100)
        return Decimal(f'{self.price}').quantize(Decimal('0.00'))


    def __str__(self):
        return self.name



class Images(models.Model):
    image = models.ImageField(upload_to='products/images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', null=True, blank=True)

    def __str__(self):
        return f'{self.product.name} {self.image.url}'

    class Meta:
        verbose_name_plural = 'Images'





class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    address = models.TextField(null=True, blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        ordering = ['-joined_at']
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'
