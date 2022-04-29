from django.conf import settings
from django.core.management.base import BaseCommand
from ...models import Account
import environ

env = environ.Env()

class Command(BaseCommand):

    def handle(self, *args, **options):
        if Account.objects.count() == 0:
            username = env("DJANGO_SUPERUSER_USERNAME")
            email = env("DJANGO_SUPERUSER_EMAIL")
            print('Creating account for %s (%s)' % (username, email))
            admin = Account.objects.create_superuser(username=username, email=email, password=env("DJANGO_SUPERUSER_PASSWORD"))
            return str(admin)
        else:
            print('Admin accounts can only be initialized if no Accounts exist')