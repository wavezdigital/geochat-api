from django.contrib.auth.models import Group, User
from rest_framework import serializers
from app.models import Profile, Favorite, Settings, Chat
from django.http import QueryDict
from rest_framework.response import Response
from django.contrib.auth import get_user_model

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['facebook_id', 'facebook_token', 'push_device_token', 'photo', 'status', 'level']

class FavoriteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Favorite
        fields = ('place_name', 'place_identifier')

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

class ChatSerializer(serializers.Serializer):
    profile_id = serializers.IntegerField()
    place_identifier = serializers.CharField(max_length=255)

    def create(self, request):
        #TODO: get profile by id and create new setting object
        profile_id = request.get('profile_id')
        profile = Profile.objects.get(id=profile_id) 
        chat = Chat.objects.create(profile=profile, **request)
        return chat

class SettingsSerializer(serializers.Serializer):
    profile_id = serializers.IntegerField()
    notification = serializers.BooleanField()

    def create(self, request):
        profile_id = request.pop('profile_id')
        profile = Profile.objects.get(id=profile_id) 
        settings = Settings.objects.create(profile=profile, **request)
        return settings