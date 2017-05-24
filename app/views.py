# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from app.models import Profile, Favorite, Chat, Settings, Complaints
from rest_framework import viewsets
from app.serializers import UserSerializer, ProfileSerializer, FavoriteSerializer, ChatSerializer, SettingsSerializer, GroupSerializer, ComplaintsSerializer
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
from django.http import HttpResponse
from rest_framework_serializer_extensions.views import SerializerExtensionsAPIViewMixin
from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response
import json
from push_notifications.models import APNSDevice, GCMDevice
from push_notifications.api.rest_framework import APNSDevice
from push_notifications.api.rest_framework import APNSDeviceSerializer

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

class ComplaintsViewSet(viewsets.ModelViewSet, SerializerExtensionsAPIViewMixin, RetrieveAPIView):
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializer
    lookup_field = 'id'

class CreateComplaintsView(CreateAPIView):
    model = Complaints
    permission_classes = (AllowAny,)
    serializer_class = ComplaintsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        count = Complaints.objects.filter(profile_receive_complaint_id=request.data['profile_receive_complaint_id']).count()
        if(count >= 2):
            profile_id = request.data['profile_receive_complaint_id'];
            profile = Profile.objects.get(id=profile_id)
            description = request.data['description']
            try:
                device = APNSDevice.objects.get(user_id=profile.user_id)
                content = {'push': 'SENDED', 'total_complaints:':count , 'complaint': serializer.data}
                device.send_message("Você Foi denunciado!", content_available=1, extra=content, sound="default")                
            except Exception as e:
                content = {'push': 'NOT_SEND', 'total_complaints:':count , 'complaint': serializer.data}
            return Response(content)
        else:
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data)

class APNSDeviceCreateViewSet(CreateAPIView):
    model = APNSDevice
    permission_classes = (AllowAny,)
    serializer_class = APNSDeviceSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['user_id'] = request.data['user_id']
        self.perform_create(serializer)
        return Response(serializer.data)

def send_push(request):
    #TODO: Android
    # device = APNSDevice.objects.get(registration_id='a18c2b07cb2fc2c083b2e8a391ea897a077918a63c60c283787a952b5792665f')
    device = APNSDevice.objects.get(user_id=2)
    device.send_message("TESTE", content_available=1, extra={"foo": "bar"})
    return HttpResponse("Device notified")