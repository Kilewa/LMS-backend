from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import ProfileSerializer
from profiles.models import Profile
from authentication.models import Users


class ProfileApi(generics.ListAPIView):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    def get_queryset(self):
        """
        This view should return a list of all the crops
        for the user.
        """
        queryset = Profile.objects.all()
        userid = self.request.query_params.get('userid', None)
        if userid is not None:
            queryset = queryset.filter(user_id=userid)
        return queryset 