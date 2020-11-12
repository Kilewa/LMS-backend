from rest_framework import serializers
from .models import task

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        exclude = ['status']

class task_statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = ['status']

