from django.test import  RequestFactory
from django.test import LiveServerTestCase
from selenium import webdriver

from config.apps.dwitter.views import dashboard


class DashboardViewTestCase(LiveServerTestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def test_base_view(self):
        request = self.factory.get('/')
        with self.assertTemplateUsed('dashboard.html'):
            res = dashboard(request)
            self.assertEqual(res.status_code, 200)

    def test_user_see_title_on_dashboard(self):
        """When user opens the dashboard, he should see the title
        'Dwitter'.
        """

        # Open the dashbaord from its url
        dashboard_page = self.browser.get(self.live_server_url + '/')
        dashboard_title = self.browser.find_element_by_css_selector('.dashboard-header')

        self.assertEqual('Dwitter', dashboard_title.text)

    def test_user_see_intro_paragraph_after_title(self):
        """After the title, the user should see an intro paragraph"""

        self.fail('Incomplete test')

    def tearDown(self) -> None:
        self.browser.quit()