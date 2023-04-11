from rest_framework import serializers
from .models import Post, PostAction, PostCategory, PostStatus
from accounts.serializers import UserGetSerializer


class PostActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAction
        fields = "__all__"


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = "__all__"


class PostStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostStatus
        fields = "__all__"



class PostSerializer(serializers.ModelSerializer):
    author = UserGetSerializer()


    class Meta:
        model = Post
        fields = "__all__"