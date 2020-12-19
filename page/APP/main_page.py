#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from common.base import BasePage
from locator.app_loc import AppLocator
from time import sleep

from page.APP.return_money.return_apply_page import ReturnApplyPage
from page.APP.return_money.return_confirm_detail_page import ReturnConfirmDetailPage
from page.APP.return_money.return_confirm_list_page import ReturnConfirmListPage
from page.APP.return_money.return_list_page import ReturnListPage


class MainPage(BasePage):
    def login_result(self):
        """查找待办业务标题是否存在,存在则登录成功"""
        todo_title = self.finds(By.XPATH, AppLocator.todo_title)
        return len(todo_title) > 0

    def switch_company(self, company):
        """切换到传入的公司"""
        self.find(By.XPATH, AppLocator.switch_company_btn).click()  # 展开切换公司列表
        self.find(By.XPATH, AppLocator.switch_target_company.format(company)).click()  # 选中一个公司
        sleep(1)
        text = self.wait_for_visible((By.XPATH, AppLocator.main_title_company)).text  # 获取页面标题
        return text == company

    def goto_module(self, module_name):
        """
        进入XX模块列表页
        :param module_name: 首页应用中的模块名称
        :return: 模块列表页面
        """
        apps_html = self.find(By.XPATH, AppLocator.icon_box).get_attribute('innerHTML')
        print('apps_html', apps_html)
        # 判断菜单是否在当前页面，在则直接跳转，不在跳转到全部菜单页面查找
        if module_name in apps_html:
            self.find(By.XPATH, AppLocator.module_name.format(module_name)).click()
        else:
            self.find(By.XPATH, AppLocator.more_icon).click()
            # 滚动页面查找菜单
            for height in range(0, 3500, 500):
                self.driver.execute_script("document.documentElement.scrollTop=" + str(height))
                element = self.finds(By.XPATH, AppLocator.module_name.format(module_name))
                if len(element) > 0:
                    element[0].click()
                    break
        # 查找跳转后的页面标题
        return_title = self.finds(By.XPATH, AppLocator.module_title.format(module_name))
        return len(return_title) > 0
        # return True

    def module_page_obj(self, module_name):
        """返回模块对应的页面对象"""
        if module_name == "回款申报":
            return ReturnListPage(self.driver)
        elif module_name == "回款确认":
            return ReturnConfirmListPage(self.driver)
        elif module_name == "销售发货":
            pass

    def module_apply_obj(self, module_name):
        """返回模块对应的申请页面对象"""
        if module_name == "回款申报":
            return ReturnApplyPage(self.driver)
        elif module_name == "销售发货":
            pass

    def module_detail_obj(self, module_name):
        """返回模块对应的详情对象"""
        if module_name == "回款确认":
            return ReturnConfirmDetailPage(self.driver)
        elif module_name == "销售发货":
            pass

    def mine(self):
        pass
