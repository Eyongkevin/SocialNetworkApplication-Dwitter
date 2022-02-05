#from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from solos.models import Solo

# Create your tests here.
class StudentTestCase(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2) # try accessing the browser for 2 minutes before timing out

        self.solo_piano = Solo.objects.create(
            track='Birthday vibe',
            artist='Kevin Enow',
            instrument='piano'
        )

        self.solo_quitter = Solo.objects.create(
            track='Love me',
            artist='Fred',
            instrument='piano'
        )


    def test_student_find_solos(self):
        """Test that a user can search for solos"""

        # live_server_url defaults to `https://localhost:8081`
        home_page = self.browser.get(self.live_server_url + '/')

        # He can see the header
        brand_element = self.browser.find_element_by_css_selector('.navbar-brand')
        self.assertEqual('Dtwitter', brand_element.text)

        # He sees the inputs of the search form, including labels and placeholders
        input_instrument = self.browser.find_element_by_css_selector('input#jmad-instrument')
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'label[for="jmad-instrument"]'
        ))
        self.assertEqual(input_instrument.get_attribute('placeholder'), 'i.e. trumpet')

        input_artist = self.browser.find_element_by_css_selector('input#jmad-artist')
        self.assertIsNotNone(self.browser.find_element_by_css_selector(
            'label[for="jmad-artist"]'
        ))
        self.assertEqual(input_artist.get_attribute('placeholder'), 'i.e. Davis')

        # He types in the name of his instrument and click on submit button
        input_instrument.send_keys('piano')
        self.browser.find_element_by_css_selector('form button').click()

        # He sees many search results, so decides to type in an artist.
        search_result = self.browser.find_elements_by_css_selector('.jmad-search-result')
        self.assertGreater(len(search_result), 1)

        input_artist = self.browser.find_element_by_css_selector('input#jmad-artist')
        input_artist.send_keys('Kevin Enow')
        self.browser.find_element_by_css_selector('form button').click()

        search_result = self.browser.find_elements_by_css_selector('.jmad-search-result')
        self.assertEqual(len(search_result), 1)

        #self.fail('Incomplete Test')

    def tearDown(self) -> None:
        self.browser.quit()