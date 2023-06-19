from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='shebelnitskiy@gmail.com',
            first_name='Admin',
            last_name='Shebel',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('134679852Se')
        user.save()