from django.urls import path
from authentication.api.views import CreateUser,VerifyAccount,LoginAPIView

urlpatterns = [
    path('register/', CreateUser.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('verifyaccount/', VerifyAccount.as_view(), name='verifyaccount'),
]