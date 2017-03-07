from django.contrib import admin
from .models import Profile, Favorite, Chat

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'status', 'level')
    fields = ['user', 'status', 'level']

admin.site.register(Profile, ProfileAdmin)

class ChatAdmin(admin.ModelAdmin):
    list_display = ('place_identifier', 'profile')
    fields = ['profile', 'place_identifier']

admin.site.register(Chat, ChatAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'place_name', 'place_identifier')
    fields = ['profile', 'place_name', 'place_identifier']

admin.site.register(Favorite, FavoriteAdmin)
