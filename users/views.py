from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from users.models import User, Pays
from users.permissions import AccountOwner
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

    def perform_create(self, serializer):
        new_user = serializer.save()

        new_user.set_password(new_user.password)
        new_user.save()

    def get_permissions(self):
        if self.action is not 'create':
            self.permission_classes = [IsAuthenticated]
            if self.action in ['update', 'retrieve', 'destroy']:
                self.permission_classes = [IsAuthenticated, AccountOwner]

        return super().get_permissions()
