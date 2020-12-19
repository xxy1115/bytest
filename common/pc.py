#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver

from common.base import BasePage
from page.PC.login_page import LoginPage


class PC(BasePage):
    def start(self):
        """启动浏览器并访问PC端网址"""
        if self.driver == None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)  # 隐式等待对所有find_element有效
            self.driver.maximize_window()
        env_data = self.parse_yaml("../data/env.yml")
        url = env_data['test_hl']['pc_url']
        self.driver.get(url)
        return LoginPage(self.driver)

    def stop(self):
        self.driver.quit()
