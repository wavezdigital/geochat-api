from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from app.models import Profile, Favorite
from django.contrib.auth.models import User

class TestProfile(TestCase):
  
    def setUp(self):
        self.user = mommy.make(User, username='usernameTest', email='test@test.com', password='12345678Ab', first_name='Teste', last_name='Wavez')
        self.profile = mommy.make(Profile, user=self.user, facebook_id='123', facebook_token='1234', level=1, status=1)

    def test_favorite_creation(self):
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertEquals(self.profile.__str__(), self.profile.name)

class TestFavorite(TestCase):

    def setUp(self):
        self.user1 = mommy.make(User, username='usernameTest', email='test1@test.com', password='12345678Ab', first_name='Teste', last_name='Wavez')
        self.profile1 = mommy.make(Profile, user=self.user1, facebook_id='123', facebook_token='1234', level=1, status=1)
        self.favorite = mommy.make(Favorite, profile=self.profile1, place_name='Cariri', place_identifier='123797912749237')
      
    def test_favorite_creation(self):
        self.assertTrue(isinstance(self.favorite, Favorite))
        self.assertEquals(self.favorite.__str__(), self.favorite.place_name)
