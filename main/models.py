from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime

from django.utils.text import slugify

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

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=100, unique=True, blank=True)
    content = models.TextField(verbose_name='Отзыв')
    preview = models.ImageField(upload_to='review_images', verbose_name='Фото', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    rating = models.IntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            suffix = 1
            self.slug = base_slug

            while Review.objects.filter(slug=self.slug).exists():
                self.slug = f'{base_slug}_{suffix}'
                suffix += 1

        super().save(*args, **kwargs)