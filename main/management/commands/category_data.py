from main.models import Category
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Очистка базы данных
        Category.objects.all().delete()


        # Заполнение данных

        category1 = Category.objects.create(name='Бытовая техника', description='Бытовая техника — электрическиемеханические приборы, которые выполняют некоторые бытовые функции, такие как приготовление пищи или чистка')
        category2 = Category.objects.create(name='ПК, ноутбуки, периферия', description='Всё для настольных ПК, комплектующие и аксессуары')
        category3 = Category.objects.create(name='Сетевое оборудование', description='Устройства, необходимые для работы компьютерной сети')
