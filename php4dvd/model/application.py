# coding: utf-8
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Application(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_home_page(self):
        self.driver.get('http://localhost/php4dvd')

    def login(self, user):
        driver = self.driver
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(user.username)
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(user.password)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)

    def logout(self):
        driver = self.driver
        driver.find_element_by_link_text('Log out').click()
        driver.switch_to_alert().accept()

    def is_logged_in(self):
        driver = self.driver
        try:
            driver.wait.until(presence_of_element_located((By.CSS_SELECTOR, 'nav')))
            return True
        except WebDriverException:
            return False

    def is_not_logged_in(self):
        driver = self.driver
        try:
            driver.wait.until(presence_of_element_located((By.ID, "loginform")))
            return True
        except WebDriverException:
            return False

    def create_movie(self, movie):
        driver = self.driver
        driver.find_element_by_partial_link_text("Add movie").click()
        driver.find_element_by_name('name').clear()
        driver.find_element_by_name('name').send_keys(movie.title)
        driver.find_element_by_name('year').clear()
        driver.find_element_by_name('year').send_keys(movie.year)
        driver.find_element_by_id('submit').click()

    def is_movie_created(self):
        driver = self.driver
        try:
            driver.wait.until(presence_of_element_located((By.XPATH, "//div[@class='maininfo_full']/h2")))
        except WebDriverException:
            return False
        actual_text = driver.find_element_by_xpath("//div[@class='maininfo_full']/h2").text.strip()
        return actual_text

    def is_not_movie_created(self):
        driver = self.driver
        try:
            driver.wait.until(presence_of_element_located((By.XPATH, "//input[@name='year']/parent::*/label")))
        except WebDriverException:
            return False
        actual_text = driver.find_element_by_xpath("//input[@name='year']/parent::*/label").text.strip()
        expected_text = 'This field is required'
        return actual_text == expected_text

    def create_movie_without_req_field(self, movie):
        driver = self.driver
        driver.find_element_by_partial_link_text("Add movie").click()
        current_url = driver.current_url
        driver.find_element_by_name('name').clear()
        driver.find_element_by_name('name').send_keys(movie.title)
        driver.find_element_by_link_text('Save').click()
        current_url_after = driver.current_url
        return current_url == current_url_after
