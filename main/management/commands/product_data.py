from main.models import Product
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Очистка базы данных
        Product.objects.all().delete()


        # Заполнение данных

        product1 = Product.objects.create(name='Техника')
        product2 = Product.objects.create(name='Продукты')
        product3 = Product.objects.create(name='Напитки')