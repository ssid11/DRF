from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from .models import User

class UserModelShortSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name','last_name')



class UserModelNameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class UserModelFullSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name','last_name', 'is_superuser', 'is_staff',)