



# class LoginView(GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
#         data = request.data
#         username = data.get('username', '')
#         password = data.get('password', '')
#         user = auth.authenticate(username=username, password=password)

#         if user:
#             auth_token = jwt.encode(
#                 {'username': user.username}, settings.JWT_SECRET_KEY)

#             serializer = UserSerializer(user)

#             data = {'user': serializer.data, 'token': auth_token}

#             return Response(data, status=status.HTTP_200_OK)

#             # SEND RES
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)