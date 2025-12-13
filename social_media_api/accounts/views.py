from django.shortcuts import render
# accounts/views.py
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from .serializers import (
    RegisterSerializer, LoginSerializer, UserSerializer, ProfileUpdateSerializer
)
from .models import User

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(id=response.data['id'])
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'user': UserSerializer(user).data, 'token': token.key}, status=status.HTTP_200_OK)

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UserSerializer(request.user).data)

    def put(self, request):
        serializer = ProfileUpdateSerializer(instance=request.user, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(UserSerializer(request.user).data)

    def patch(self, request):
        serializer = ProfileUpdateSerializer(instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(UserSerializer(request.user).data)

class FollowView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            target = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        if target == request.user:
            return Response({'detail': 'Cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        target.followers.add(request.user)
        return Response({'detail': f'You now follow {target.username}.'}, status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        try:
            target = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        target.followers.remove(request.user)
        return Response({'detail': f'You unfollowed {target.username}.'}, status=status.HTTP_200_OK)
