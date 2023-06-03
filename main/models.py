from django.db import models
from django.utils import timezone
from datetime import datetime

NULLABLE = {'blank': True, 'null': True}
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Продукт')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='product_images',verbose_name='Фото', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=100, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}\n{self.description}'

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews',on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    preview = models.ImageField(upload_to='review_images', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    rating = models.IntegerField()
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title