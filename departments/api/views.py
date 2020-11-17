from rest_framework import generics, response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from authentication.models import User
from authentication.api.utils import Util
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from authentication.api.serializers import RegisterSerializer, LoginSerializer
import jwt
from django.conf import settings
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from departments.models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentListView(generics.ListAPIView):
    """Define service to get departments list"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeCreateView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all employees.

    post:
    Create a new employee.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data
            user = User.objects.get(email=user_data['email'])

            token=RefreshToken.for_user(user).access_token

            current_site = get_current_site(request).domain

            relativeLink = reverse('verifyaccount')

            absurl='http://'+current_site+relativeLink+"?token="+str(token)
            email_body = 'Hi '+user.username+' use link below to verify your email: \n'+ absurl
            data={'email_body':email_body,'to_user':user.email, 'email_subject': 'Account Activation'}

            Util.send_email(data)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDeleteView(generics.DestroyAPIView):
    """delete:
    Delete an employee.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer