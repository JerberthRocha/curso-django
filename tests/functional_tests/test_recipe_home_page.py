from django.contrib.staticfiles.testing import StaticLiveServerTestCase 
from utils.browser import make_chrome_browser
from selenium.webdriver.common.by import By
from time import sleep


class RecipeHomeFunctionalTest(StaticLiveServerTestCase):
    def test_the_test(self):
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        sleep(3)
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No recipes found here', body.text)
        browser.quit()