from rest_framework.viewsets import ModelViewSet
from .models import ToDo, Project
from .serializers import ToDoModelSerializer, ProjectModelSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, \
   DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter, ToDoFilter

class ToDoPaginator(LimitOffsetPagination):
    default_limit = 20


class ProjectPaginator(LimitOffsetPagination):
    default_limit = 10

class ToDoModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, \
   DestroyModelMixin, GenericViewSet):
   queryset = ToDo.objects.all()
   serializer_class = ToDoModelSerializer
   # pagination_class = ToDoPaginator
   filterset_class = ToDoFilter

   def perform_destroy(self, instance):
      instance.active = False
      instance.save()


class ProjectModelViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectModelSerializer
   # pagination_class = ProjectPaginator
   filterset_class = ProjectFilter
