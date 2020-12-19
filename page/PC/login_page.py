#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from common.base import BasePage
from locator.pc_loc import PCLocator
from time import sleep

from page.PC.main_page import MainPage
from utils.helper import Helper


class LoginPage(BasePage):
    def login(self, username, password, company):
        """登录PC"""
        self.find(By.XPATH, PCLocator.username).clear()
        self.find(By.XPATH, PCLocator.username).send_keys(username)
        self.find(By.XPATH, PCLocator.password).clear()
        self.find(By.XPATH, PCLocator.password).send_keys(password)
        self.find(By.XPATH, PCLocator.company_input).click()  # 展示公司列表
        self.find(By.XPATH, PCLocator.li_span_text.format(company)).click()  # 选择传入的公司
        self.find(By.XPATH, PCLocator.captcha_input).send_keys(self.__get_captcha())  # 输验证码
        self.find(By.XPATH, PCLocator.login_btn).click()
        return MainPage(self.driver)

    def __get_captcha(self):
        key = self.find(By.XPATH, PCLocator.captcha_input).get_attribute("data-key")
        return Helper.parse_captcha(key)
