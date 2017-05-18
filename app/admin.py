from django.contrib import admin
from .models import Profile, Favorite, Chat, User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_name', 'status', 'level')
    fields = ['status', 'level']
    def get_user_name(self, obj):
    	return obj.user.username
    get_user_name.short_description= "User Name"

admin.site.register(Profile, ProfileAdmin)

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id','place_identifier', 'profile')
    fields = ['profile', 'place_identifier']

admin.site.register(Chat, ChatAdmin)

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id','get_profile_name', 'place_name', 'place_identifier', 'address')
    fields = [ 'place_name', 'place_identifier', 'address']

    def get_profile_name(self, obj):
    	user_profile = User.objects.get(id=obj.profile.user_id)
    	return user_profile.username
    get_profile_name.short_description = "User Name"


admin.site.register(Favorite, FavoriteAdmin)
