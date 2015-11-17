# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from basic_actions import BasicAction


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

    def test_search_movie(self):
        driver = self.driver
        # create movie
        action = BasicAction(driver)
        action.create_movie('Terminator', 1984)
        action.create_movie('Midnight in Paris', 2011)

        # make search valid movie
        driver.get(self.url)
        driver.find_element_by_id('q').clear()
        driver.find_element_by_id('q').send_keys("Midnight in Paris")
        driver.find_element_by_id('q').send_keys(Keys.RETURN)
        find_result = driver.find_element_by_class_name("title").text
        self.assertEqual(find_result, 'Midnight in Paris')
        time.sleep(2)

        # make search invalid movie
        driver.find_element_by_id('q').clear()
        driver.find_element_by_id('q').send_keys("Midnight in Barcelona")
        driver.find_element_by_id('q').send_keys(Keys.RETURN)
        find_result = driver.find_element_by_class_name("content").text
        self.assertEqual(find_result, 'No movies where found.')
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()  # test runner
