#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from common.base import BasePage
from locator.app_loc import AppLocator


class ReturnListPage(BasePage):
    def search(self, serial_number):
        """列表页搜索/验证单据信息"""
        self.find(By.XPATH, AppLocator.head_btn_right1).click()
        # self.driver.execute_script('document.querySelectorAll(".uni-inputs")[0].lastChild.textContent="2020-12-20"')#无效。改变日期需要选择器中确认
        self.find(By.XPATH, AppLocator.uni_button_confirm).click()
        return_list_item = self.find(By.XPATH, AppLocator.return_list_item.format(serial_number))
        customer = return_list_item.find_element(By.CSS_SELECTOR, '.returned_company span').text
        money_str = return_list_item.find_element(By.CSS_SELECTOR, '.warnColor span').text
        money = float(money_str.split('¥')[1])
        status = return_list_item.find_element(By.CSS_SELECTOR, '.invoice_status').text
        return {"customer": customer, "money": money, "status": status}

    def goto_apply(self):
        """跳转到申请页面"""
        self.find(By.XPATH, AppLocator.head_btn_right2).click()
        # 查找跳转后的页面标题
        title = self.finds(By.XPATH, AppLocator.module_title.format("回款申报申请"))
        return len(title) > 0
