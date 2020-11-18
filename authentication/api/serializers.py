from rest_framework import serializers
from authentication.models import User
from django.contrib.auth import get_user_model
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


User = get_user_model()

class LoginSerializer(serializers.ModelSerializer):
    '''
    Login Serializer
    '''
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=70, min_length=5, write_only=True)
    username = serializers.CharField(max_length=255, read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_dept_head = serializers.BooleanField(read_only=True)
    tokens = serializers.CharField(max_length=255, read_only=True)


    class Meta:
        model = User
        fields=['email','is_staff', 'is_dept_head','password','username','tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Account Does Not Exist')
        if not user.is_active:
            raise AuthenticationFailed('Account Disabled, Contact Admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email Not Verified')
        
        return {
            'email':user.email,
            'username': user.username,
            'is_staff': user.is_staff,
            'is_dept_head': user.is_dept_head,
            'tokens': user.tokens()
        
        }
        # return super().validate(attrs)