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

    def test_create_movie(self):
        driver = self.driver
        driver.find_element_by_partial_link_text("Add movie").click()
        driver.find_element_by_name('name').send_keys('The Terminal')
        driver.find_element_by_name('year').send_keys('2004')
        driver.find_element_by_id('submit').click()

        actual_text = driver.find_element_by_xpath("//div[@class='maininfo_full']/h2").text.strip()
        expected_text = "The Terminal (2004)"
        self.assertEqual(actual_text, expected_text)
        # time.sleep(5)

    def test_uncreate_movie(self):
        driver = self.driver
        driver.find_element_by_partial_link_text("Add movie").click()
        current_url = driver.current_url
        driver.find_element_by_name('name').send_keys('The Terminal')
        driver.find_element_by_link_text('Save').click()

        current_url_after = driver.current_url
        actual_text = driver.find_element_by_xpath("//input[@name='year']/parent::*/label").text.strip()
        expected_text = 'This field is required'
        self.assertEqual(current_url, current_url_after)
        self.assertEqual(actual_text, expected_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()  # test runner

