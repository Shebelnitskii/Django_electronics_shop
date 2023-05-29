from django.shortcuts import render

from main.models import Product


# Create your views here.
def home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'main/home.html', context)
