from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from app.models import Profile, Favorite
from rest_framework import viewsets
from app.serializers import UserSerializer, GroupSerializer, ProfileSerializer, FavoriteSerializer
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from material.frontend.views import ModelViewSet

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