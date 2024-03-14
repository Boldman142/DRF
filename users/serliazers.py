from users.models import User, Pays

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pays
        fields = '__all__'
