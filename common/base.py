#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator=None):
        """
        查找元素.支持传入一个元组的形式
        :param by: 元素定位方式
        :param locator: 元素定位路径
        :return: 元素对象
        """
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def finds(self, by, locator=None):
        if locator is None:
            result = self.driver.find_elements(*by)
        else:
            result = self.driver.find_elements(by, locator)
        return result

    def wait_for_click(self, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return element

    def wait_for_visible(self, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))
        return element

    def parse_yaml(self, path):
        with open(path, encoding="utf-8") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
