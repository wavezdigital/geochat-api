from django.contrib.auth.models import Group, User
from rest_framework import serializers
from app.models import Profile, Favorite, Settings, Chat, Complaints
from django.http import QueryDict
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework_serializer_extensions.serializers import SerializerExtensionsMixin

class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Profile
        fields = ['id','facebook_id', 'facebook_token', 'push_device_token', 'photo', 'status', 'level', 'username', 'email']

        def get(self, request, *args, **kwargs):
            profile = self.get_object()
            return profile

class FavoriteSerializer(serializers.HyperlinkedModelSerializer):
    profile_id = serializers.IntegerField()
    place_name = serializers.CharField(max_length=255)
    place_identifier = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255,  default='NO_ADDRESS_ENTERED')

    class Meta:
        model = Favorite
        fields = ('id','place_name', 'place_identifier', 'profile_id', 'address')

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

class ChatSerializer(serializers.Serializer):
    profile_id = serializers.IntegerField()
    place_identifier = serializers.CharField(max_length=255)

    class Meta:
        model = Profile
        fields = ('facebook_id', 'user_id', 'level', 'status', 'photo')
        expandable_fields = dict(
            profile=ProfileSerializer
        )

    def create(self, request):
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

class ComplaintsSerializer(serializers.HyperlinkedModelSerializer):
    profile_denouncing_id = serializers.IntegerField()
    profile_receive_complaint_id = serializers.IntegerField()
    place_identifier = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    complaint_date = serializers.DateTimeField()

    class Meta:
        model = Complaints
        fields = ('id', 'profile_denouncing_id', 'profile_receive_complaint_id', 'place_identifier', 'description', 'complaint_date') 
