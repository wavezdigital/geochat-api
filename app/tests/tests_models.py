from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime
from app.models import Profile, Favorite, Chat, Settings
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

class TestChat(TestCase):
  
    def setUp(self):
        self.user2 = mommy.make(User, username='usernameTest', email='test@test.com', password='12345678Ab', first_name='Teste', last_name='Wavez')
        self.profile2 = mommy.make(Profile, user=self.user2, facebook_id='123', facebook_token='1234', level=1, status=1)
        self.chat = mommy.make(Chat, profile=self.profile2, place_identifier='123')

    def test_favorite_creation(self):
        self.assertTrue(isinstance(self.chat, Chat))
        self.assertEquals(self.chat.__str__(), self.chat.place_identifier)

class TestSettings(TestCase):
  
    def setUp(self):
        self.user3 = mommy.make(User, username='usernameTest', email='test@test.com', password='12345678Ab', first_name='Teste', last_name='Wavez')
        self.profile3 = mommy.make(Profile, user=self.user3, facebook_id='123', facebook_token='1234', level=1, status=1)
        self.settings = mommy.make(Settings, profile=self.profile3, notification=True)

    def test_favorite_creation(self):
        self.assertTrue(isinstance(self.settings, Settings))
        self.assertEquals(self.settings.__str__(), self.settings.notification)