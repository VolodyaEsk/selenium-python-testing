class Application(object):

    url = "http://rozetka.com.ua/"

    def __init__(self, driver):
        self.driver = driver

    def go_to_home_page(self):
        self.driver.get(self.url)

    def search_product(self, product):
        driver = self.driver
        search_field = driver.find_element_by_name("text")
        search_field.click()
        search_field.clear()
        search_field.send_keys(product)
        search_button = driver.find_element_by_name("search-button")
        search_button.click()