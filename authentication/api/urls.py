from django.urls import path
from authentication.api.views import VerifyAccount,LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('verifyaccount/', VerifyAccount.as_view(), name='verifyaccount'),
]