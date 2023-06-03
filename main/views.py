from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from main.models import Product, Category, Review


# Create your views here.
# def products(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list
#     }
#     return render(request, 'main/product_list.html', context)

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'


class ProductListView(generic.View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'main/product_list.html', {'products': products})


# def categories(request):
#     products_list = Category.objects.all()
#     context = {
#         'object_list': products_list
#     }
#     return render(request, 'main/category_list.html', context)

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'main/category_list.html'
    context_object_name = 'object_list'




class ProductReviewListView(generic.ListView):
    template_name = 'main/reviews.html'
    context_object_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_pk = self.kwargs['pk']
        product = get_object_or_404(Product, pk=product_pk)
        context['product'] = product
        return context

    def get_queryset(self):
        product_pk = self.kwargs['pk']
        return Review.objects.filter(product=product_pk)



class ReviewCreateView(generic.CreateView):
    model = Review
    template_name = 'main/review_form.html'
    fields = '__all__'


class ReviewDetailView(generic.DetailView):
    template_name = 'main/review_detail.html'
    context_object_name = 'reviews'
    name = 'review_detail.html'

    def get(self, request, *args, **kwargs):
        review = self.get_object()
        review.views_count += 1
        review.save()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        review_id  = self.kwargs['pk']
        return Review.objects.filter(pk=review_id )


class ReviewUpdateView(generic.UpdateView):
    model = Review
    template_name = 'main/review_form.html'
    fields = '__all__'


class ReviewDeleteView(generic.DeleteView):
    model = Review
    template_name = 'main/review_confirm_delete.html'
    success_url = reverse_lazy('main:review_list')

