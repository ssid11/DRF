from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ToDo, Project
from .serializers import ToDoModelSerializer, ProjectModelSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, \
   DestroyModelMixin

class ToDoModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, \
   DestroyModelMixin, GenericViewSet):
   queryset = ToDo.objects.all()
   serializer_class = ToDoModelSerializer

   def perform_destroy(self, instance):
      instance.active = False
      instance.save()


class ProjectModelViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectModelSerializer
