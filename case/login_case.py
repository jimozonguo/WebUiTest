import unittest
from drivers.page import Page
import time

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_page = Page(pagefile="loginpage", browser_type='chrome').get("http://www.spsin.com")
        cls.home_page = Page(page=cls.login_page, pagefile="homepage")

    @classmethod
    def tearDownClass(cls):
        cls.login_page.quit()

    def tearDown(self):
        self.login_page.screen_shot()

    def test01(self):
        self.login_page.page_el("username_by_xpath").send_keys("admin888")
        self.login_page.page_el("password_by_xpath").send_keys("888888")
        self.login_page.page_el("loginbotton_by_xpath").click()
        self.home_page.page_el("car_by_xpath").click()



if __name__  ==  '__main__':
    unittest.main()
