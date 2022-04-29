from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post
from accounts.serializers import UserSerializer
from accounts.models import UserManagement
from rest_framework.serializers import Serializer, FileField

class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['post_img']



class PostSerializer(serializers.ModelSerializer):
    """docstring for Postserializer."""
    tweet = serializers.CharField(
        max_length=150,
        min_length=2,
        allow_blank=True,
        trim_whitespace=True
    )
    created = serializers.HiddenField(default=timezone.now)
    user_id=serializers.CharField(required=False)

    class Meta:
        model = Post
        fields = ('tweet', 'created', 'post_img', 'user_id')

    def create(self, validated_data):
        request = self.context.get("request")
        # print(request.user.id)
        user = UserManagement.objects.get(user=request.user.id)
        post = Post.objects.create(
            tweet=validated_data['tweet'],
            created=validated_data['created'],
            post_img=validated_data['post_img'],
            user_id=user
        )
        post.save()

        return post
