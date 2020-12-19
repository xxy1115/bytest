#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from common.base import BasePage
from locator.app_loc import AppLocator
from time import sleep


class CustomerPage(BasePage):
    def customer(self, customer_name):
        """选择客户"""
        self.find(By.XPATH, AppLocator.search_input).send_keys(customer_name)
        self.find(By.XPATH, AppLocator.search_btn).click()
        customer_item = self.finds(By.XPATH, AppLocator.customer_item_title.format(customer_name))
        customer_item[0].click()
