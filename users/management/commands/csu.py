# from django.core.management import BaseCommand
#
# from users.models import User
#
#
# class Command(BaseCommand):
#
#     def handle(self, *args, **options):
#         user = User.objects.create(
#             email='moderator@test.com',
#             is_staff=True,
#         )
#         user.set_password('123456789')
#         user.save()


import redis

try:
    # Установка подключения к серверу Redis
    r = redis.Redis(host='localhost', port=6379)

    # Проверка соединения
    response = r.ping()
    if response:
        print("Соединение с сервером Redis успешно установлено.")
    else:
        print("Не удалось установить соединение с сервером Redis.")
except redis.ConnectionError:
    print("Ошибка подключения к серверу Redis.")