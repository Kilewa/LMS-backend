from django.http import HttpResponse,Http404
from rest_framework.views import APIView
from django.shortcuts import render,redirect,reverse
from rest_framework import generics, permissions, mixins,status
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token_generator import account_activation_token
from .serializer import *
from .models import CustomUser as User,Departmenthead,Employee
from lmsproject.settings import UIDOMAIN

#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User has been successfully registered.Verify email address to activate account!',
                'user': serializer.data
            }

            return Response(response, status=status_code)

#Account activation API
def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_verified = True
        user.save()
        login(request, user)
        context={
        'success':True,
        'user':user,
        'domain':UIDOMAIN,
        'status':'success',
        'message':'Email Successfully Verified!',
        }
        return render(request,'activation_status.html',context)
    else:
        context={
        'success':False,
        'status':'danger',
        'message':'Activation link is invalid!',
        }
        return render(request,'activation_status.html',context)       



#Login API
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }

            return Response(response, status=status_code)  





class DepartmentheadListView(generics.ListAPIView):
    queryset = Departmenthead.objects.all()
    serializer_class = DeptSerializer


class DepartmentheadView(APIView):
    def get_dept(self, deptid):
        try:
            return Departmenthead.objects.get(user_id=deptid)
        except Departmenthead.DoesNotExist:
            return Http404

    def get(self, request, deptid, format=None):
        departmenthead = self.get_dept(deptid)
        serializers = DeptSerializer(departmenthead)
        return Response(serializers.data) 


    def put(self, request, deptid, format=None):
        departmenthead = self.get_dept(deptid)
        serializer = DeptSerializer(departmenthead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request, deptid, format=None):
        departmenthead = self.get_dept(deptid)
        departmenthead.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  




class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeView(APIView):
    def get_emp(self, empid):
        try:
            return Employee.objects.get(user_id=empid)
        except Employee.DoesNotExist:
            return Http404

    def get(self, request, empid, format=None):
        employee = self.get_emp(empid)
        serializers = EmployeeSerializer(employee)
        return Response(serializers.data) 


    def put(self, request, empid, format=None):
        employee = self.get_emp(empid)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request, empid, format=None):
        employee = self.get_emp(empid)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

