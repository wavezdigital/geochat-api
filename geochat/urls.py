"""geochat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.conf.urls import url, include
from django.views import generic
from rest_framework import routers
from app import views
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Square API')

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'favorites', views.FavoriteViewSet)

urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'register/$', views.CreateUserView.as_view(), name='user'),
    url(r'validate-email/$', views.UserListByEmailView.as_view(), name='validate_email'),
    url(r'favorite-by-profile-id/(?P<profile_id>\d+)/$', views.FavoriteByProfileId.as_view(), name='favorite_by_profile_id'),
    url(r'settings/$', views.CreateSettingsView.as_view(), name='settings'),
    url(r'push/$', views.send_push, name='push'),
    url(r'new-profile/$', views.CreateProfileView.as_view(), name='profile'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/$', schema_view),
]
