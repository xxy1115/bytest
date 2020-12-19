#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from common.base import BasePage
from locator.app_loc import AppLocator


class ReturnConfirmDetailPage(BasePage):
    def approve(self):
        self.find(By.XPATH, AppLocator.head_btn_right1).click()
        self.find(By.XPATH, AppLocator.menu_approve).click()
        self.find(By.XPATH, AppLocator.approve_msg).send_keys("已审核")
        self.find(By.XPATH, AppLocator.pass_btn).click()




