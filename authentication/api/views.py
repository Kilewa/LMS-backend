from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import User
from authentication.api.serializers import RegisterSerializer
from .permissions import IsDepartmentHead, IsEmployee
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CreateUser(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data

            return Response(user_data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
