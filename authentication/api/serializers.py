

from rest_framework import serializers
from authentication.models import Users


class RegistrationSerializer(serializers.ModelSerializer):
    '''
    creating registration serializer
    '''
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = Users
        fields = ['email','username', 'password','password2']
        extra_kwargs = {
            'password': {'write_only':True}
        }
    def save(self):
        authentication = Users(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match.'})
        authentication.set_password(password)
        authentication.save()
        return authentication
