from django.urls import path
from authentication.api.views import CreateUser,VerifyAccount

urlpatterns = [
    path('register/', CreateUser.as_view(), name='register'),
    path('verifyaccount/', VerifyAccount.as_view(), name='verifyaccount'),
]