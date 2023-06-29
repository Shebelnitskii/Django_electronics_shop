from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import ProductForm, VersionForm

from main.models import Product, Category, Review, Version



class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'main/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.object.name} {self.object.description}"
        return context


class ProductListView(generic.ListView):
    model = Product
    template_name = 'main/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        versions = Version.objects.filter(product__in=context['products'], is_current=True)
        context['versions'] = versions
        return context


class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()

        self.object.owner = self.request.user
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main:product_list')

class ProductUpdateView(UserPassesTestMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main/product_form.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        else:
            return self.form_invalid(form)
        return super().form_valid(form)

    def is_moderator(self):
        return self.request.user.groups.filter(name='manager').exists()

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return user == product.owner or (self.is_moderator() and user.is_authenticated)

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())

class ProductPublishView(generic.View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if request.user.is_staff and product.is_published == False:
            product.is_published = True
            product.save()
        else:
            product.is_published = False
            product.save()
        return redirect('main:product_list')

class ProductDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'main/product_confirm_delete.html'
    permission_required = 'main.delete_product'

    def get_success_url(self):
        return reverse('main:product_list')

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'main/category_list.html'
    context_object_name = 'object_list'
    extra_context = {'title': 'Категории'}


class ProductReviewListView(generic.ListView):
    extra_context = {'title': 'Отзывы'}
    template_name = 'main/reviews_list.html'
    context_object_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_pk = self.kwargs['pk']
        product = get_object_or_404(Product, pk=product_pk)
        context['product'] = product
        context['title'] = f"Отзыв на товар: {product.name} {product.description}"
        return context

    def get_queryset(self):
        product_pk = self.kwargs['pk']
        return Review.objects.filter(product=product_pk, is_published=True)


class ReviewCreateView(generic.CreateView):
    model = Review
    template_name = 'main/review_form.html'
    fields = ('author', 'title', 'content', 'preview')
    extra_context = {'title': 'Оставить отзыв'}

    def get_success_url(self):
        return reverse('main:product_reviews', kwargs={'pk': self.kwargs['pk']})

    def get_initial(self):
        initial = super().get_initial()
        initial['product'] = self.kwargs['pk']
        return initial

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)


class ReviewUpdateView(generic.UpdateView):
    model = Review
    template_name = 'main/review_form.html'
    fields = ('author', 'title', 'content', 'preview')
    extra_context = {'title': 'Изменить отзыв'}

    def get_success_url(self):
        return reverse('main:product_reviews', kwargs={'pk': self.object.product_id})

    def get_initial(self):
        initial = super().get_initial()
        initial['product'] = self.kwargs['pk']
        return initial

    def form_valid(self, form):
        return super().form_valid(form)


class ReviewDetailView(generic.DetailView):
    template_name = 'main/review_detail.html'
    context_object_name = 'reviews'
    name = 'review_detail.html'

    def get(self, request, *args, **kwargs):
        review = self.get_object()
        review.views_count += 1
        review.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Отзыв: {context['reviews'].author}"
        return context

    def get_queryset(self):
        review_id = self.kwargs['pk']
        return Review.objects.filter(pk=review_id)


class ReviewDeleteView(generic.DeleteView):
    model = Review
    template_name = 'main/review_confirm_delete.html'
    extra_context = {'title': 'Подтвердите удаление'}

    def get_success_url(self):
        return reverse_lazy('main:product_reviews', kwargs={'pk': self.object.product_id})
