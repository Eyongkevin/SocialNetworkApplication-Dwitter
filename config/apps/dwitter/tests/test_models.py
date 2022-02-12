from django.test import TestCase
from config.apps.dwitter.models import Profile 
from django.contrib.auth.models import User


class ProfileModelTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create(username='kevin')
    
    def test_profile_created(self):
        self.assertTrue(Profile.objects.filter(user__username= 'kevin').exists())
    
    def test_profile_follows_self(self):
        self.kevin_profile = Profile.objects.get(user__username= 'kevin')

        self.assertIn(self.kevin_profile, self.kevin_profile.follows.all())
