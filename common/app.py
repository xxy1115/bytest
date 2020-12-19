#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.base import BasePage
from locator.app_loc import AppLocator
from page.APP.login_page import LoginPage


class App(BasePage):
    def start(self):
        """启动浏览器并访问APP网址"""
        if self.driver == None:
            options = webdriver.ChromeOptions()
            mobile_emulation = {'deviceName': 'iPhone 6/7/8'}
            options.add_experimental_option('mobileEmulation', mobile_emulation)
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)  # 隐式等待对所有find_element有效
            # self.driver.set_window_size(1920, 1080)
            self.driver.maximize_window()
        env_data = self.parse_yaml("../data/env.yml")
        url = env_data['test_hl']['app_url']
        self.driver.get(url)
        self.close_popup()
        return LoginPage(self.driver)

    def stop(self):
        self.driver.quit()

    def close_popup(self):
        """关闭服务协议和隐私政策弹窗"""
        list = self.finds(By.XPATH, AppLocator.approve_text)
        if len(list) > 0:
            self.find(By.XPATH, AppLocator.approve_text).click()
