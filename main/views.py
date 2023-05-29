from django.shortcuts import render

from main.models import Product, Category


# Create your views here.
def products(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'main/products.html', context)

def categories(request):
    products_list = Category.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'main/categories.html', context)
