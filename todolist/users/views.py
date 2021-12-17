from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from .models import User
from .serializers import UserModelSerializer, UserModelSerializerShort


class UserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin,  CreateModelMixin, GenericViewSet):
   queryset = User.objects.all()
   # serializer_class = UserModelSerializer
   serializer_class = UserModelSerializerShort

   def get_serializer_class(self):
      if self.request.version == '2.0':
         return UserModelSerializer
      return UserModelSerializerShort


class UserListAPIView(generics.ListAPIView):
   queryset = User.objects.all()
   serializer_class = UserModelSerializer

   def get_serializer_class(self):
      if self.request.version == '2.0':
         return UserModelSerializer
      return UserModelSerializerShort
