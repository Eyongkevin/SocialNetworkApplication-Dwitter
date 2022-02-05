from django.test import TestCase

from solos.models import Solo


class SoloModelTestCase(TestCase):
    def setUp(self) -> None:
        self.solo = Solo.objects.create(
            track='Birthday vibe',
            artist='Kevin Enow',
            instrument='piano'
        )

    def test_solo_basic(self):
        self.assertEqual(self.solo.artist, 'Kevin Enow')