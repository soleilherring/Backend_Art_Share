from django.shortcuts import render,redirect
from rest_framework import viewsets, permissions, exceptions
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        name= serializer.validated_data.get('name')

        try:
            user= User.objects.get(email=email, password=password, name=name)
        except User.DoesNotExist:
            return Response({'message': 'Login failed'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'category', 'title','date', 'condition','reserved']

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reviewer', 'reviewed_user', 'post']

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


