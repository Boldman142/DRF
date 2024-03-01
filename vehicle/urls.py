from django.urls import path

# from vehicle.views import
from vehicle.apps import VehicleConfig
from rest_framework.routers import DefaultRouter

from vehicle.views import CarViewSet

app_name = VehicleConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')


urlpatterns = [
    # path('', ..., name='login')

] + router.urls
