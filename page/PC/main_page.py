#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from common.base import BasePage
from time import sleep

from locator.pc_loc import PCLocator


class MainPage(BasePage):
    def login_result(self):
        """登录成功提示是否显示"""
        login_success_msg = self.finds(By.XPATH, PCLocator.login_success_msg)
        return len(login_success_msg) > 0

    def sale_app(self):
        pass

    def mine(self):
        pass
