""" Tests the whole automation process. """
import time
from unittest import TestCase

from main import Automater


class Test(TestCase):
    """ Test automation process """

    def setUp(self):
        self.automater = Automater()
        self.browser = self.automater.browser

    def tearDown(self):
        self.automater.tear_down()

    def test(self):
        """ Tests the automation system """
        # Test login process
        self.automater.login()
        classrooms = self.browser.find_elements_by_css_selector(
            '.onkcGd.kj3hr.YVvGBb')
        self.assertEqual(len(classrooms), 2)

        # Tests whether the process goes to video panel
        self.automater.login()
        self.automater.go_to_weekly_video_panel()
        time.sleep(5)
        self.assertEqual(self.browser.title, 'Weekly Video')

        # Test data scraping
        self.automater.login()
        self.automater.go_to_weekly_video_panel()
        data = self.automater.scrape_data('student')
        for item in data:
            self.assertEqual(len(item), 3)
