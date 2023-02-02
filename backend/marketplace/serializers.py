# # translates between python and json
from rest_framework import serializers
from .models import Post, User, PostImage, Category, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # variable that reperesnts list of items 
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('posts', "name", "id")

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only=True)
    # category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ["id","title", "images", "description", "location", "category", "reserved", "uploaded_images", "user"]


    # def create(self, validated_data):
    #     uploaded_images = validated_data.pop('uploaded_images')
    #     post = Post.objects.create(**validated_data)
    #     category_data = validated_data.pop('category')
    #     for image in uploaded_images:
    #         newpost_image = PostImage.objects.create(post=post, image=image)
    #     for category_item in category_data:
    #         category = Category.objects.get(id=category_item['id'])
    #         post.category.add(category)
    #     return post
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        category_data = validated_data.pop('category')
        print(category_data)

        post = Post.objects.create(**validated_data)
        for image in uploaded_images:
            newpost_image = PostImage.objects.create(post=post, image=image)

        # # for category_item in category_data:
        # category = Category.objects.filter(name=category_data)
        # print("this is the category queryset", category)
        # post.category.set(category)
        category = Category.objects.get(name__in=category_data)
        post.category.add(category)

        return post
    
    # def partial_update(self, validated_data):
    #     print('inside update')
    #     if validated_data['uploaded_images']:
    #         uploaded_images = validated_data.pop('uploaded_images')
        
    #     if validated_data['category_data']:
    #         category_data = validated_data.pop('category')
        
    #     post = Post.objects.update(**validated_data)
    #     for image in uploaded_images:
    #         newpost_image = PostImage.objects.create(post=post, image=image)

    #     for category_item in category_data:
    #         category = Category.objects.filter(name=category_item)
    #         post.category.set(category)

    #     return post




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'