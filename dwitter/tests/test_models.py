from django.test import TestCase
from dwitter.models import Profile 
from django.contrib.auth.models import User


class ProfileModelTestCase(TestCase):
    def setUp(self) -> None:
        self.user_kevin = User.objects.create(username='kevin')
        self.user_tassimo = User.objects.create(username='tassimo')

        self.tassimo_profile = Profile.objects.create(user=self.user_tassimo)
        self.kevin_profile = Profile.objects.create(user=self.user_kevin)

        self.kevin_profile.follows.add(self.tassimo_profile)

    
    def test_profile_created(self):
        self.assertEqual(self.kevin_profile.user.username, 'kevin')
    
    def test_profile_has_followers(self):
        self.assertIn(self.tassimo_profile, self.kevin_profile.follows.all())

    def test_profile_no_followers(self):
        self.assertFalse(self.tassimo_profile.follows.all().exists())