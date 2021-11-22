from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import ToDo, Project

class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        # fields = ('username', 'email', 'first_name','last_name')
        fields = ('id', 'project', 'author', 'text','on_created', 'on_edit', 'active',  )


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        # fields = ('', 'email', 'first_name','last_name')
        fields = ('id', 'name', 'repo', 'devops', )