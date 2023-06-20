from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from main.models import NULLABLE
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    is_verified = models.BooleanField(default=False, verbose_name='Верифицирован')



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class EmailVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
