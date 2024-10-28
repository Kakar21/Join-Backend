from django.shortcuts import render
from rest_framework import generics, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import RegistrationSerializer, UserProfileSerializer, EmailAuthSerializer
from .models import UserProfile


class UserProfileList(generics.ListCreateAPIView):
    """
    List or create user profiles.
    
    - **GET**: Returns all user profiles.
    - **POST**: Creates a new user profile.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific user profile.
    
    - **GET**: Retrieves a profile.
    - **PUT/PATCH**: Updates a profile.
    - **DELETE**: Deletes a profile.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CustomLoginView(ObtainAuthToken):
    """
    Log in a user with email and password, returning a token.
    """
    permission_classes = [AllowAny]
    serializer_class = EmailAuthSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        data = {}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'id': user.id,
                'token': token.key,
                'username': user.username,
                'email': user.email,
            }
            return Response(data, status=200)
        else:
            return Response(serializer.errors, status=400)


class RegistrationView(APIView):
    """
    Register a new user and return a token.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account)
            data = {
                'id': saved_account.id,
                'token': token.key,
                'username': saved_account.username,
                'email': saved_account.email,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
