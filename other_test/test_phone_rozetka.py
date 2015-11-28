# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium_fixture import app


def test_rozetka(app):
    app.go_to_home_page()
    app.search_product("Samsung Galaxy S6 SS 32GB G920 Black")
    app.driver.find_element_by_link_text("Samsung Galaxy S6 SS 32GB G920 Black").click()

