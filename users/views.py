# from django.contrib.auth.views import LoginView as BaseLogin
# from django.contrib.auth.views import LogoutView as BaseLogout
# from django.views.generic import CreateView, UpdateView
# from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
# from rest_framework import viewsets

from users.models import User, Pays
from users.serliazers import UserSerializer, PaysSerializer


class PaysListApiView(generics.ListAPIView):
    serializer_class = PaysSerializer
    queryset = Pays.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('date_pay', 'pay_course', 'pay_lesson', 'way_pay')
    ordering_fields = ('date_pay',)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# class LoginView(BaseLogin):
#     pass
#
#
# class LogoutView(BaseLogout):
#     pass
#
#
# class RegisterView(CreateView):
#     model = User
#     success_url = reverse_lazy('users:login')
#
#
# class UserUpdateView(UpdateView):
#     model = User
#     success_url = reverse_lazy('users:profile')
#
#     def get_object(self, queryset=None):
#         return self.request.user
