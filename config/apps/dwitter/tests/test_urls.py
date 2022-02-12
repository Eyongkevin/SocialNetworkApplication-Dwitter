from django.test import TestCase
from django.urls import resolve

from config.apps.dwitter.views import dashboard


class DashboardURLTestCase(TestCase):
    def test_index_url(self):
        root = resolve('/')
        self.assertEqual(root.func, dashboard)