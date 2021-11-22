from django.db import models
from users.models import User

class Project(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название проекта',unique=True)
    repo = models.URLField(verbose_name='Сыллка на репозиторий')
    devops = models.ManyToManyField(User,verbose_name='Разработчики')

    def __str__(self):
        return self.name


class ToDo(models.Model):
    text = models.TextField(max_length=1024, verbose_name='Текст заметки',blank=False)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, verbose_name='Название проекта')
    author = models.OneToOneField(User,verbose_name='Автор заметки',on_delete=models.PROTECT)
    on_created = models.DateTimeField(auto_now_add=True)
    on_edit = models.DateTimeField(auto_now=True)
    active = models.BooleanField(verbose_name='Активна?', default=True)
