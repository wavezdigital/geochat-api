from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from app.models import Profile, Favorite, Chat, Settings
from rest_framework import viewsets
from app.serializers import UserSerializer, ProfileSerializer, FavoriteSerializer, ChatSerializer, SettingsSerializer, GroupSerializer
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
from push_notifications.models import APNSDevice, GCMDevice
from django.http import HttpResponse
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
from rest_framework import filters
from rest_framework import generics



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProfileViewSet(viewsets.ModelViewSet, SerializerExtensionsAPIViewMixin, RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class UserListByEmailView(ListAPIView):
    model  = User
    serializer_class = UserSerializer
    def get_queryset(self):
        response = User.objects.filter( email = self.request.GET['email'] )
        return response

class FavoriteByProfileId(ListAPIView):
    model  = Favorite
    serializer_class = FavoriteSerializer
    def get_queryset(self):
        response = Favorite.objects.filter( profile_id = self.kwargs['profile_id'] )
        return response

class CreateProfileView(CreateAPIView):
    model = Profile
    permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer

class CreateSettingsView(CreateAPIView):
    model = Settings
    permission_classes = (AllowAny,)
    serializer_class = SettingsSerializer

class CreateChatView(CreateAPIView):
    model = Chat
    permission_classes = (AllowAny,)
    serializer_class = ChatSerializer

def send_push(request):
    #TODO: Android
    device = APNSDevice.objects.get(registration_id='ecf8943dc2b0b20a9f7b98e2584b20f647793613fa7d91367f935165986829ab')
    device.send_message("TESTE", content_available=1, extra={"foo": "bar"}, sound="default")
    return HttpResponse("Device notified")