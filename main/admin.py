from django.contrib import admin
from .models import Category, Product, Review, Version


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
    list_display = ['id', 'author', 'product', 'slug', 'rating', 'views_count', 'created_at']
    list_filter = ('product', 'views_count', 'is_published',)
    fields = ['author', 'title', 'content', 'preview']


admin.site.register(Review, ReviewAdmin)

class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'version_number', 'version_name', 'is_current')
    list_filter = ('product', 'version_number', 'version_name', 'is_current')
    fields = ['product', 'version_number', 'version_name', 'is_current']

admin.site.register(Version, VersionAdmin)
