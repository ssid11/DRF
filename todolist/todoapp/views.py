from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ToDo, Project
from .serializers import ToDoModelSerializer, ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
   queryset = ToDo.objects.all()
   serializer_class = ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectModelSerializer
