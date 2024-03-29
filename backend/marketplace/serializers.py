# # translates between python and json
from rest_framework import serializers
from .models import Post, User, PostImage, Category, Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('posts', "name", "id")
        depth = 1

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    category_list = serializers.CharField(write_only=True)
    images = PostImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only=True)

    class Meta:
        model = Post
        fields = ["id","title", "images", "description", "location", "category_list", "reserved", "uploaded_images", "user_id", "date", "user", "condition"]
        depth = 1

    def create(self, validated_data, *args, **kwargs):
        uploaded_images = validated_data.pop('uploaded_images')
        category_data = validated_data.pop('category_list')

        post = super().create(validated_data, *args, **kwargs)
        for image in uploaded_images:
            newpost_image = PostImage.objects.create(post=post, image=image)

        category_data_list = category_data.split(',')
        categories = Category.objects.filter(name__in=category_data_list)
        for category_item in categories:
            post.category.add(category_item)

        return post



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    name = serializers.CharField()