from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='moderator@test.com',
            is_staff=True,
        )
        user.set_password('123456789')
        user.save()