from django.urls import path
from main.views import ProductListView, ProductDetailView, CategoryListView
from main.views import (
    ProductReviewListView,
    ReviewCreateView,
    ReviewDetailView,
    ReviewUpdateView,
    ReviewDeleteView,
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'
urlpatterns = [
    path('reviews/<int:pk>/', ProductReviewListView.as_view(), name='product_reviews'),
    path('reviews/create/', ReviewCreateView.as_view(), name='review_create'),
    path('reviews/<int:pk>/review_detail/', ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/<slug:slug>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/<slug:slug>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('', CategoryListView.as_view(), name='category_list')
] + staticfiles_urlpatterns()
