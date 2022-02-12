from django.test import TestCase, RequestFactory
from django.urls import resolve

from config.apps.dwitter.views import dashboard


class DashboardViewTestCase(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_base_view(self):
        request = self.factory.get('/')
        with self.assertTemplateUsed('dashboard.html'):
            res = dashboard(request)
            self.assertEqual(res.status_code, 200)