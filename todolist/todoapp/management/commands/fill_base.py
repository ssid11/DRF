from django.core.management.base import BaseCommand
from users.models import User
from todoapp.models import Project, ToDo

class Command(BaseCommand):
    def handle(self, *args, **options):
        ToDo.objects.all().delete()
        Project.objects.all().delete()
        User.objects.all().delete()
        admin = User.objects.create_user(username='admin',email='t1@a.com',password='1')
        dev = User.objects.create_user(username='dev', email='t2@a.com',password='1')
        owner = User.objects.create_user(username='owner', email='t3@a.com',password='1')
        su = User.objects.create_superuser(username='su',email='a@b.com',password='1')

        project1 = Project()
        project2 = Project()

        project1.name = 'Project 1'
        project1.repo = 'https://github.com/ssid11/DRF/'
        project1.save()
        project1.devops.add(admin)
        project1.save()

        project2.name = 'Project 2'
        project2.repo = 'https://github.com/ssid11/DRF/'
        project2.save()
        project2.devops.add(dev,owner)
        project2.save()

        todo1 = ToDo()
        todo2 = ToDo()
        todo3 = ToDo()

        todo1.text = 'ToDo 1 Text'
        todo1.project = project1
        todo1.author = admin
        todo1.save()

        todo2.text = 'ToDo 2 Text'
        todo2.project = project2
        todo2.author = dev
        todo2.save()

        todo3.text = 'ToDo 2_1 Text'
        todo3.project = project2
        todo3.author = owner
        todo3.save()

