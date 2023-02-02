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


    # def create(self, request):
    # create permission class for protecting things someone owns and when creating post
    # make sure items belong to  user
    # in reacct, when doing create post, will grab items endpoint and pass in user id
    # api/items?owner_id={user_id}
    

    
    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True

    #     if request.user == None: 
    #         raise exceptions.NotAuthenticated()
            
    #     for item_id in request.data["items"]:
    #         if Item.objects.exclude(owner_id=request.user.id).filter(pk=item_id):
    #             raise exceptions.PermissionDenied() 
        
    #     return super().update(request, *args, **kwargs)

# update and filtering 

    # def get_queryset(self):
    #     queryset = self.queryset
    #     query_set = queryset.filter(id=self.request.user.id)
        # return query_set

    # permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     return Post.objects.filter(id=self.request.user.id)

    
    
        # return Post.objects.filter(items__id=self.request.user.id)

    # def get_queryset(self):
    #     user = self.request.user
    #     items = Item.objects.filter(owner=user)
    #     posts = Post.objects.filter(items__in=items)
    #     return posts

    # def create_post(request, user_id):
    #     user = User.objects.get(id=user_id)
    #     items = Item.objects.filter(owner=user)
    #     return JsonResponse({'items': items})


# class PostIViewSet(viewsets.ModelViewSet):
#     serializer_class = ItemSerializer
#     queryset = Item.objects.all()

#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['owner', 'category', 'condition']

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


