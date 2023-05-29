from django.urls import path
from main.views import products, categories
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
                  path('', products, name='products'),
                  path('categories/', categories)] + staticfiles_urlpatterns()
