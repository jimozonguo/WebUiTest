from utils.config import Config
import os
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]


class PageEl:

    def __init__(self, page):
        pageelymlfile = Config().get('pageelymlfile')
        elpage = Config(os.path.join(BASE_PATH, 'pageel', pageelymlfile+".yml")).get(page)
        self.el = Config(os.path.join(BASE_PATH, 'pageel', elpage+".yml"))

    def get(self, el):
        eltype=el.split('_')[2]
        if eltype == 'xpath':
            el = "(By.XPATH,'" + self.el.get("pageel")[el] + "')"
        if eltype == 'ID':
            el = "(By.ID,'" + self.el.get("pageel")[el] + "')"
        return el

if __name__ == "__main__":
    s = PageEl('loginpage').get('username_by_xpath')
    print(s)
