from django.contrib.auth.models import Group, User
from rest_framework import serializers
from app.models import Profile, Favorite
from django.http import QueryDict
from rest_framework.response import Response
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('username', 'email')

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=255)
    # email = serializers.EmailField(max_length=255)
    # password = serializers.CharField(max_length=255)

    def create(self, request):
        username = request.get('username')
        email = request.get('email')
        password = request.get('password')
        status = request.get('status')
        level = request.get('level')
        facebook_id = request.get('facebook_id')
        facebook_token = request.get('facebook_token')
        
        user = UserSerializer.create(username, **request)
        profile = Profile.objects.create(user=user, status=status, level=level, facebook_id=facebook_id, facebook_token=facebook_token, push_device_token=123)

        return profile

    class Meta:
        model = Profile
        fields = ['facebook_id', 'facebook_token', 'push_device_token', 'photo', 'status', 'level']

        model = User
        fields = ['username', 'email', 'password']

class FavoriteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Favorite
        fields = ('place_name', 'place_identifier')
