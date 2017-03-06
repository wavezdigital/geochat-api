from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    facebook_id = models.CharField(max_length=255)
    facebook_token = models.CharField(max_length=255)
    push_device_token = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    level = models.IntegerField() #default: 0- standard/1- superuser
    status = models.IntegerField() #default: 1- Active/0- inactive/2- Ban

    #to get the full name of user instance
    def name(self):
        return self.user.first_name + ' ' + self.user.last_name
    name.short_description = "Name"
    full_name = property(name)

    def __str__(self):
        return self.name

class Favorite(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile')
    place_name = models.CharField(max_length=255)
    place_identifier = models.CharField(max_length=255)

    def name(self):
        return self.profile.user.first_name + ' ' + self.profile.user.last_name
    name.short_description = "Name"
    full_name = property(name)

    def __str__(self):
        return self.place_name