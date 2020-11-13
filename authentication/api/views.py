from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authentication.models import User
from authentication.api.serializers import UserSerializer


class CreateUser(APIView):
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)

        if serializer.is_valid():

            user = serializer.save()
            response="successfully registered new user"
            email =user.email
            username =user.username
            role=user.role

            return Response(response,email,username,role, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
