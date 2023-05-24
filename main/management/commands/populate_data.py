from main.models import Category
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Очистка базы данных
        Category.objects.all().delete()


        # Заполнение данных

        category1 = Category.objects.create(name='Техника')
        category2 = Category.objects.create(name='Продукты')
        category3 = Category.objects.create(name='Напитки')
