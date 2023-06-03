from django.contrib import admin
from .models import Category, Product, Review


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


admin.site.register(Product, ProductAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'rating', 'views_count', 'created_at']
    list_filter = ('product', 'views_count',)

admin.site.register(Review, ReviewAdmin)