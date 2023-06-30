from django.urls import path
from django.views.decorators.cache import cache_page

from main.views import ProductListView, ProductDetailView, CategoryListView, ProductPublishView
from main.views import (
    ProductReviewListView,
    ReviewCreateView,
    ReviewDetailView,
    ReviewUpdateView,
    ReviewDeleteView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'
urlpatterns = [
    path('reviews_list/<int:pk>/', ProductReviewListView.as_view(), name='product_reviews'),
    path('review_form/<int:pk>/', ReviewCreateView.as_view(), name='review_create'),
    path('reviews_list/<int:pk>/review_detail/', ReviewDetailView.as_view(), name='review_detail'),
    path('review_form/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('review_form/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/publish/', ProductPublishView.as_view(), name='product_publish'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('product_form/', ProductCreateView.as_view(), name='product_create'),
    path('product_form/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product_form/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('', CategoryListView.as_view(), name='category_list')
] + staticfiles_urlpatterns()
