from django.contrib import admin
from .models import Profile, Favorite

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'status', 'level')
    fields = ['user', 'status', 'level']

admin.site.register(Profile, ProfileAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'place_name', 'place_identifier')
    fields = ['profile', 'place_name', 'place_identifier']

admin.site.register(Favorite, FavoriteAdmin)
