from rest_framework import serializers
from authentication.models import Users

""" class UserSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Users
        fields = ['email','username']

    def save(self):
        authentication = Users(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        authentication.save()
        return authentication """

class UserSerializer(serializers.ModelSerializer):
    '''
    creating registration serializer
    '''
    class Meta:
        model = Users
        fields = ['email','username']
        
    def save(self):
        authentication = Users(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        authentication.save()
        return authentication
