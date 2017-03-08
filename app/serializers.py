from django.contrib.auth.models import Group, User
from rest_framework import serializers
from app.models import Profile, Favorite
from django.http import QueryDict
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin

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
        expandable_fields = dict(
            profile=ProfileSerializer
        )

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user