import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('c:\\tmp\\chromedriver.exe')
        self.drv.get('http://google.com/ncr')

    def test_search(self):
        assert 'Google' in self.drv.title
        gsearch = self.drv.find_element_by_name('q')
        gsearch.send_keys('selenide')
        gsearch.send_keys(Keys.RETURN)
        rs = self.drv.find_elements_by_xpath('//*[@id="rso"]/div')
        assert 'Selenide' in rs[0].text
        hdtb = self.drv.find_elements_by_xpath('//*[@id="hdtb-msb-vis"]/div')
        img_button = hdtb[1]
        img_button.click()
        rs = self.drv.find_elements_by_xpath('//*[@id="islrg"]/div/div/a[2]')
        assert 'selenide.org' in rs[0].text
        hdtb = self.drv.find_elements_by_xpath('//a[@class="NZmxZe"]')
        img_button = hdtb[0]
        img_button.click()
        rs = self.drv.find_elements_by_xpath('//*[@id="rso"]/div')
        assert 'Selenide' in rs[0].text

    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
