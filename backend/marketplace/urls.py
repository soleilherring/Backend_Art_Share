# from django.urls import path
# from . import views

# urlpatterns =[
#     path('', views.userList, name="users")
# ]

from rest_framework import routers
from .views import *
# ReviewViewSet, ProfileViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'api/posts', PostViewSet, 'posts')  
router.register(r'api/items', ItemViewSet, 'items')
router.register(r'api/reviews', ReviewViewSet, 'reviews') 
router.register(r'api/profiles', ProfileViewSet, 'profiles') 
router.register(r'api/categories', CategoryViewSet, 'categories') 

urlpatterns = router.urls