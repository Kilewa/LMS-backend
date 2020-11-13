from rest_framework import serializers
from authentication.models import Users
from profiles.models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'          