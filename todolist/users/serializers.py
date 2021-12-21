from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import User

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name','last_name')


class UserModelSerializerShort(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)