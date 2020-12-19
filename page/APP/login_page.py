#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from common.base import BasePage
from locator.app_loc import AppLocator
from time import sleep

from page.APP.main_page import MainPage
from selenium.webdriver import ActionChains


class LoginPage(BasePage):
    def login(self, username, password):
        """登录APP"""
        env_data = self.parse_yaml("../data/env.yml")
        ip = env_data['test_hl']['ip']
        port = env_data['test_hl']['port']
        self.switch_ip(ip, port)
        self.find(By.XPATH, AppLocator.username).clear()
        self.find(By.XPATH, AppLocator.username).send_keys(username)
        self.find(By.XPATH, AppLocator.password).clear()
        self.find(By.XPATH, AppLocator.password).send_keys(password)
        self.find(By.XPATH, AppLocator.password).click()  # 增加一次点击操作，解决密码没输入完成就提交的问题
        approve_checkbox = self.find(By.XPATH, AppLocator.approve_checkbox).get_attribute("class")
        if ("check" in approve_checkbox) and ("checked" not in approve_checkbox):
            approve_checkbox.click()
        self.find(By.XPATH, AppLocator.login_btn).click()
        return MainPage(self.driver)

    def switch_ip(self, ip="", port=""):
        """切换IP和端口号"""
        self.find(By.XPATH, AppLocator.switch_ip_link).click()
        # input_ip = self.find(By.XPATH, AppLocator.input_ip)
        # input_port = self.find(By.XPATH, AppLocator.input_port)
        # self.driver.execute_script('arguments[0].value=""', input_ip)  # clear()偶尔清除不了
        # self.find(By.XPATH, AppLocator.input_ip).send_keys(ip)
        # self.driver.execute_script('arguments[0].value=""', input_port)
        # self.find(By.XPATH, AppLocator.input_port).send_keys(port)
        self.find(By.XPATH, AppLocator.input_ip).clear()
        self.find(By.XPATH, AppLocator.input_ip).send_keys(ip)
        self.find(By.XPATH, AppLocator.input_port).click()  # 输入ip后点击端口输入框，端口号可能自动带出，且清除不完全
        self.find(By.XPATH, AppLocator.input_port).clear()
        self.find(By.XPATH, AppLocator.input_port).send_keys(port)
        self.find(By.XPATH, AppLocator.input_port).click()  # 增加一次点击操作，避免端口输入不完整
        self.find(By.XPATH, AppLocator.switch_ip_btn).click()
