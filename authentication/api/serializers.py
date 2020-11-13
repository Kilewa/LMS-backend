from rest_framework import serializers
from authentication.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    '''
    creating registration serializer
    '''
    class Meta:
        model = User
        fields = ['email','username','role']
        
    def save(self):
        authentication = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        authentication.save()
        return authentication
