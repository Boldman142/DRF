from django.urls import path

# from users.views import
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    #     path('', ..., name='login')

]