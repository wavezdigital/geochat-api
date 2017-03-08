from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from app.models import Profile, Favorite, Chat, Settings
from rest_framework import viewsets
from app.serializers import UserSerializer, GroupSerializer, ProfileSerializer, FavoriteSerializer, ChatSerializer, SettingsSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView, 
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView
    )
from rest_framework.permissions import AllowAny
from material.frontend.views import ModelViewSet
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
# from rest_framework.mixins import UpdateModelMixin

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
            

class FavoriteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class CreateProfileView(CreateAPIView):
    model = Profile
    permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer

class ListProfileView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class DetailProfileAPIView(SerializerExtensionsAPIViewMixin, RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class profileUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

    # model = User
    # queryset = Profile.objects.all()
    # serializer_class = UserSerializer

class profileDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class CreateChatView(CreateAPIView):
    model = Chat
    permission_classes = (AllowAny,)
    serializer_class = ChatSerializer

class CreateSettingsView(CreateAPIView):
    model = Settings
    permission_classes = (AllowAny,)
    serializer_class = SettingsSerializer
