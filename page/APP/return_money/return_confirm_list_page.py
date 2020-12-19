#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from common.base import BasePage
from locator.app_loc import AppLocator
from page.APP.return_money.return_confirm_detail_page import ReturnConfirmDetailPage


class ReturnConfirmListPage(BasePage):
    def search(self, serial_number, name=""):
        """
        列表页搜索/验证单据信息
        :param serial_number:必传
        :param name:申请人姓名,可选
        :return:
        """
        self.find(By.XPATH, AppLocator.head_btn_right1).click()
        self.find(By.XPATH, AppLocator.applyer).send_keys(name)
        self.find(By.XPATH, AppLocator.uni_button_confirm).click()
        return_list_item = self.find(By.XPATH, AppLocator.return_list_item.format(serial_number))
        customer = return_list_item.find_element(By.CSS_SELECTOR, '.returned_company span').text
        money_str = return_list_item.find_element(By.CSS_SELECTOR, '.apply_money span').text
        money = float(money_str.split('¥ ')[1])
        return {"customer": customer, "money": money}

    def goto_detail(self):
        """跳转到详情页面"""
        self.find(By.XPATH, AppLocator.return_serial_number).click()
        return ReturnConfirmDetailPage()
