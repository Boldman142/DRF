# from django.contrib.auth.views import LoginView as BaseLogin
# from django.contrib.auth.views import LogoutView as BaseLogout
# from django.views.generic import CreateView, UpdateView
# from django.urls import reverse_lazy

from rest_framework import viewsets

from users.models import User
from users.serliazers import UserSerializer


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
