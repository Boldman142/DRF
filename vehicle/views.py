from rest_framework import viewsets

from vehicle.models import Car
from vehicle.serliazers import CarSerializers


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializers
    queryset = Car.objects.all()
