# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class CreateMovie(unittest.TestCase):

    login = 'admin'
    password = 'admin'

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.url = 'http://localhost/php4dvd'
        self.driver.get(self.url)
        self.driver.find_element_by_id('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys(Keys.RETURN)

    def test_delete_movie(self):

        # create movie
        driver = self.driver
        driver.find_element_by_partial_link_text("Add movie").click()
        driver.find_element_by_name('name').send_keys('Everest')
        driver.find_element_by_name('year').send_keys('2015')
        driver.find_element_by_id('submit').click()

        # delete this movie
        driver.find_element_by_partial_link_text("Remove").click()
        alert = driver.switch_to_alert();
        alert.accept()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()  # test runner
