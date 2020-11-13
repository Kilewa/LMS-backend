from django.urls import path
from authentication.api.views import CreateUser


app_name = 'authentication'


urlpatterns = [
    path('register/', CreateUser.as_view(), name="register"),
]