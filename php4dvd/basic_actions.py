# coding: utf-8


class BasicAction(object):

    def __init__(self, driver):
        self.driver = driver

    def create_movie(self, title, year):
        driver = self.driver
        driver.find_element_by_partial_link_text("Add movie").click()
        driver.find_element_by_name('name').send_keys(title)
        driver.find_element_by_name('year').send_keys(year)
        driver.find_element_by_id('submit').click()
        driver.get('http://localhost/php4dvd')

