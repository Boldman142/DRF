from django.urls import path
from rest_framework import routers

from users.views import UserViewSet, PaysListApiView

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('pay/', PaysListApiView.as_view(), name='pay_list')
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', UserUpdateView.as_view(), name='profile')
]
router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns += router.urls
