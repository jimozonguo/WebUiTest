import unittest
from drivers.page import Page

class TestLogin(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    @classmethod
    def setUpClass(cls):
        cls.home_page = Page(pagefile="homepage", browser_type='chrome').get("https://www.baidu.com/")
        cls.journalism_page = Page(page=cls.home_page, pagefile="journalismpage")

    @classmethod
    def tearDownClass(cls):
        cls.home_page.quit()

    def tearDown(self):
        self.home_page.screen_shot()

    def test01(self):
        self.home_page.page_el("journalism_by_xpath").click()
        self.journalism_page.page_el("girl_by_xpath").click()
        self.journalism_page.page_el("baiduinput_by_xpath").send_keys("蔡依林")
        self.journalism_page.page_el("baidubotton_by_xpath").click()


if __name__  ==  '__main__':
    unittest.main()
