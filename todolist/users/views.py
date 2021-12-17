from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import User
from .serializers import UserModelFullSerializer, UserModelShortSerializer


class UserModelViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserModelFullSerializer

   def get_serializer_class(self):
      if self.request.version == 'v2':
         return UserModelFullSerializer
      return UserModelShortSerializer



