from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from authentication.api.serializers import RegisterSerializer, LoginSerializer
import jwt
from django.conf import settings
from .permissions import IsDepartmentHead, IsEmployee
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .send_email import send_mail

class CreateUser(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data
            user = User.objects.get(email=user_data['email'])
        
            token=RefreshToken.for_user(user).access_token

            current_site = get_current_site(request).domain

            relativeLink = reverse('verifyaccount')

            absurl='http://'+current_site+relativeLink+"?token="+str(token)

            send_mail(user, absurl)

            return Response(user_data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyAccount(APIView):
    def get(self,request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token,settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email':'Successfully activated'},status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error':'Activation Link Expired'},status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error':'Invalid Token'},status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)