from  django.urls import path
from main.views import home
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'

urlpatterns = [
    path('', home, name = 'home')] + staticfiles_urlpatterns()