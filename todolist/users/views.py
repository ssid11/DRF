from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import User
from .serializers import UserModelSerializer


# class UserModelViewSet(ModelViewSet):
# class UserModelViewSet(GenericAPIView):
class UserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
   queryset = User.objects.all()
   serializer_class = UserModelSerializer
