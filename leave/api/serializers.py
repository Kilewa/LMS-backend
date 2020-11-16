from rest_framework import serializers
from .models import leave

class leaveSerializer(serializers.ModelSerializer):


    class Meta:
        model = leave
        fields = '__all__'


class approve_leaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = leave
        fields = ['status','comments']

