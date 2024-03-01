from rest_framework import serializers

from vehicle.models import Car, Moto


class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'
