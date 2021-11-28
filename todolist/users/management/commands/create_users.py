from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        User.objects.create_user(username='Test1',email='t1@a.com')
        User.objects.create_user(username='Test2', email='t2@a.com')
        User.objects.create_user(username='Test3', email='t3@a.com')
        User.objects.create_superuser(username='su',email='a@b.com',password='1')
        for idx in range(4,200,1):
            User.objects.create_user(username='Test' + str(idx), email='Test' + str(idx)+'@a.com')

