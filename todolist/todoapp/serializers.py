from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import ToDo, Project



class ToDoModelSerializer(ModelSerializer):

    class Meta:
        model = ToDo
        fields = ('id', 'project', 'author', 'text','on_created', 'on_edit', 'active',  )



class ProjectModelSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'repo', 'devops', )