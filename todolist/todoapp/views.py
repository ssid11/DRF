from rest_framework.viewsets import ModelViewSet
from .models import ToDo, Project
from .serializers import ToDoModelSerializer, ProjectModelSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, \
   DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter, ToDoFilter



class ToDoModelViewSet(ModelViewSet):
   queryset = ToDo.objects.all()
   serializer_class = ToDoModelSerializer


   def perform_destroy(self, instance):
      instance.active = False
      instance.save()


class ProjectModelViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectModelSerializer

