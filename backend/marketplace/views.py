from django.shortcuts import render,redirect
# from django.http import HttpResponse
from rest_framework import viewsets, permissions, exceptions
from .serializers import *
from .models import *
# from django.http import JsonResponse
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend


# def userList(request):
#     return HttpResponse("make a user")
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'category', 'title','date']

    # def create(self, request, *args, **kwargs):

    #         if request.user == None: 
    #             raise exceptions.NotAuthenticated()

    #         for item_id in request.data["items"]:
    #             if Item.objects.exclude(owner_id=request.user.id).filter(pk=item_id):
    #                 raise exceptions.PermissionDenied() 
            
    #         return super().create(request, *args, **kwargs)
    
    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True

    #     if request.user == None: 
    #         raise exceptions.NotAuthenticated()
            
    #     for item_id in request.data["items"]:
    #         if Item.objects.exclude(owner_id=request.user.id).filter(pk=item_id):
    #             raise exceptions.PermissionDenied() 
        
    #     return super().update(request, *args, **kwargs)

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


