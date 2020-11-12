from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authentication.models import Users
from authentication.api.serializers import UserSerializer

""" 
class CreateUser(APIView):
      def post(self, request):
          user = request.data
          serializer = UserSerializer(data=user)

          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)

          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """


@api_view(['POST',])
def CreateUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
                authentication = serializer.save()
                data['response']="successfully registered new user"
                data['email'] = authentication.email
                data['username'] = authentication.username
        else:
                data = serializer.errors
        return Response(data)