from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet

from solos.views import index
from solos.models import Solo

# Create your tests here.

class SolosIndexTextCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()

        self.solo_piano = Solo.objects.create(
            track='Birthday vibe',
            artist='Kevin Enow',
            instrument='piano'
        )

        self.solo_quitter = Solo.objects.create(
            track='Love me',
            artist='Fred',
            instrument='guitter'
        )

    def test_index_view_basic(self):
        """
        Test that index view returns a 200 response and uses the correct template
        """

        request = self.factory.get('/')
        with self.assertTemplateUsed('solos/index.html'):
            res = index(request)
            self.assertEqual(res.status_code, 200)

    def test_index_view_returns_solos(self):
        """
        Test that the index view will attempt to return Solos if query parameters exist
        """

        res = self.client.get('/', {'instrument':'piano'})
        solos = res.context['solos']
        self.assertIs(
            type(solos),
            QuerySet
        )
        self.assertEqual(len(solos), 1)
        self.assertEqual(solos[0].artist, 'Kevin Enow')