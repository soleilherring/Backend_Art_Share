from django.urls import path
# from . import views

# urlpatterns =[
#     path('', views.userList, name="users")
# ]

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'api/posts', PostViewSet, 'posts')  
# router.register(r'api/items', ItemViewSet, 'items')
router.register(r'api/reviews', ReviewViewSet, 'reviews') 
router.register(r'api/users', UserViewSet, 'users') 
router.register(r'api/categories', CategoryViewSet, 'categories') 
# 
urlpatterns = router.urls