#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from common.base import BasePage
from locator.app_loc import AppLocator
from time import sleep

from page.components.customer_page import CustomerPage
from selenium.webdriver import ActionChains
import time


class ReturnApplyPage(BasePage):
    def choose_customer(self, customer_name):
        """验证客户"""
        self.find(By.XPATH, AppLocator.choose_customer).click()
        CustomerPage(self.driver).customer(customer_name)
        text = self.find(By.XPATH, AppLocator.choose_customer).text
        return text == customer_name

    def choose_pay_type(self, pay_type):
        """验证付款方式"""
        self.find(By.XPATH, AppLocator.choose_pay_type).click()
        pay_type_path = self.find(By.XPATH, AppLocator.picker_option.format(pay_type))
        confirm_btn = self.find(By.XPATH, AppLocator.picker_confirm_btn)
        action = ActionChains(self.driver)  # 直接click报错： element not interactable
        action.move_to_element(pay_type_path).click().move_to_element(confirm_btn).click()
        sleep(1)
        action.perform()
        # confirm_btn = self.find(By.XPATH, AppLocator.picker_confirm_btn)
        # self.driver.execute_script('arguments[0].click()', confirm_btn)  # 解决元素被遮挡问题
        text = self.find(By.XPATH, AppLocator.pay_type_text).text
        return text == pay_type

    def choose_bank(self, bank_name):
        """验证收款银行"""
        self.find(By.XPATH, AppLocator.choose_bank).click()
        bank_path = self.find(By.XPATH, AppLocator.picker_option.format(bank_name))
        confirm_btn = self.find(By.XPATH, AppLocator.picker_confirm_btn)
        action = ActionChains(self.driver)
        action.move_to_element(bank_path).click().move_to_element(confirm_btn).click()
        sleep(1)
        action.perform()
        text = self.find(By.XPATH, AppLocator.bank_text).text
        return text == bank_name

    def input_payer(self, payer):
        """验证付款人"""
        self.find(By.XPATH, AppLocator.payer).send_keys(payer)
        text = self.find(By.XPATH, AppLocator.payer).get_attribute("value")
        return text == payer

    def input_pay_account(self, account):
        """验证付款账号"""
        self.find(By.XPATH, AppLocator.pay_account).send_keys(account)
        text = self.find(By.XPATH, AppLocator.pay_account).get_attribute("value")
        return text == account

    def choose_return_type(self, return_type):
        """验证回款类型"""
        self.driver.execute_script("document.documentElement.scrollTop=400")
        self.find(By.XPATH, AppLocator.choose_return_type).click()
        type_path = self.find(By.XPATH, AppLocator.picker_option.format(return_type))
        confirm_btn = self.find(By.XPATH, AppLocator.picker_confirm_btn)
        action = ActionChains(self.driver)
        action.move_to_element(type_path).click().move_to_element(confirm_btn).click()
        sleep(1)
        action.perform()
        text = self.find(By.XPATH, AppLocator.return_type_text).text
        return text == return_type

    def choose_product_line(self, product_line):
        """验证产品线"""
        self.find(By.XPATH, AppLocator.choose_product_line).click()
        # 生产环境有搜索框
        # self.find(By.XPATH, AppLocator.search_input).send_keys(product_line)
        # self.find(By.XPATH, AppLocator.search_btn).click()
        product_line_item = self.finds(By.XPATH, AppLocator.product_line_item.format(product_line))
        product_line_item[0].click()
        text = self.find(By.XPATH, AppLocator.product_line_text).text
        return text == product_line

    def choose_product(self, product):
        """验证产品名称"""
        self.find(By.XPATH, AppLocator.choose_product_name).click()
        for item in product:
            self.find(By.XPATH, AppLocator.search_input).clear()
            self.find(By.XPATH, AppLocator.search_input).send_keys(item["product_code"])
            self.find(By.XPATH, AppLocator.search_input).click()
            self.find(By.XPATH, AppLocator.search_btn).click()
            # inner_html = self.find(By.XPATH, AppLocator.son_content).get_attribute("innerHTML")
            # if inner_html == "":
            #     refresh_span = self.finds(By.XPATH, AppLocator.refresh_span)
            #     if len(refresh_span) > 0:
            #         refresh_span[0].click()
            # 频繁请求接口时无返回数据，列表空，点击刷新
            refresh_span = self.finds(By.XPATH, AppLocator.refresh_span)
            if len(refresh_span) > 0:
                refresh_span[0].click()
            checkbox_ele = self.find(By.XPATH, AppLocator.product_item_checkbox.format(item["product_name"]))
            check_status = checkbox_ele.get_attribute("class")
            if 'checked' not in check_status:
                checkbox_ele.click()
        self.find(By.XPATH, AppLocator.product_confirm_btn).click()

    def add_money(self, money_item):
        """新增款项"""
        for index in range(len(money_item) - 1):
            self.find(By.XPATH, AppLocator.add_text).click()  # 新增款项行
        money_item_tr = self.finds(By.XPATH, AppLocator.money_item_tr)
        expected_money = 0
        for index, item in enumerate(money_item_tr):
            item.find_element(By.CSS_SELECTOR, 'uni-picker').click()
            money_type = self.find(By.XPATH, AppLocator.picker_option.format(money_item[index]['type']))
            confirm_btn = self.find(By.XPATH, AppLocator.picker_confirm_btn)
            action = ActionChains(self.driver)
            action.move_to_element(money_type).click().move_to_element(confirm_btn).click()
            sleep(1)
            action.perform()
            item.find_element(By.CSS_SELECTOR, 'input').send_keys(money_item[index]['money'])
            expected_money += money_item[index]['money']
        ele = self.find(By.XPATH, AppLocator.return_money)
        ele.click()
        actual_money = ele.text
        return expected_money == float(actual_money)

    def check_price_policy(self, price_policy):
        """验证价格政策"""
        text = self.find(By.XPATH, AppLocator.price_policy_span).text
        return text == price_policy

    def view_activity(self, activity):
        """验证优惠活动"""
        self.find(By.XPATH, AppLocator.view_activity).click()
        flag = True
        for index, item in enumerate(activity):
            activity_name = self.finds(By.XPATH, AppLocator.activity_name.format(item['name']))
            if len(activity_name) == 0:
                print(f"优惠活动:{item['name']} 未展示")
                flag = False
        self.find(By.XPATH, AppLocator.back_icon).click()
        return flag

    def choose_credit(self, credit):
        """验证欠款核销"""
        self.find(By.XPATH, AppLocator.choose_credit).click()
        expected_credit_money = 0
        if 'overdue' in credit and len(credit['overdue']) > 0:  # 到期额度单据
            # self.find(By.XPATH, AppLocator.credit_tab_overdue).click()
            for item in credit['overdue']:
                self.scroll_check_input(item)
                expected_credit_money += item['use_money']
            self.find(By.XPATH, AppLocator.uni_button_confirm).click()
        if 'notdue' in credit and len(credit['notdue']) > 0:  # 未到期额度单据
            sleep(1)
            self.find(By.XPATH, AppLocator.credit_tab_notdue).click()
            for item in credit['notdue']:
                self.scroll_check_input(item)
                expected_credit_money += item['use_money']
            self.find(By.XPATH, AppLocator.uni_button_confirm).click()
        actual_credit_money = self.find(By.XPATH, AppLocator.choose_credit).text
        return expected_credit_money == float(actual_credit_money)

    def check_and_input(self, item):
        """(用于页面未做分页时)
        查找单据，找到后滚动到可视区域，勾选单据并输入本次核销
        :param item:传入单据数组
        """
        card = self.finds(By.XPATH, AppLocator.credit_card.format(item['serial_number']))
        if len(card) > 0:  # card[0]为单号所在卡片组
            checkbox_ele = card[0].find_element(By.CSS_SELECTOR, '.check')
            check_status = checkbox_ele.get_attribute("class")
            if 'checked' not in check_status:
                self.driver.execute_script("arguments[0].scrollIntoView(false)", card[0])
                checkbox_ele.click()

            # 自定义等待方法(等待勾选核销单后自动带出本次核销金额，再做清空和输入操作)
            def wait_not_zero(x: WebDriver):
                try:
                    input_ele = card[0].find_element(By.CSS_SELECTOR, 'input')
                    value_str = input_ele.get_attribute('value')
                    return value_str != "0"
                except:
                    return False

            WebDriverWait(self.driver, 10).until(wait_not_zero)
            card[0].find_element(By.CSS_SELECTOR, 'input').clear()
            card[0].find_element(By.CSS_SELECTOR, 'input').send_keys(item['use_money'])
            card[0].find_element(By.CSS_SELECTOR, 'input').click()

    def scroll_check_input(self, item):
        """(用于页面滚动分页时)
        滚动页面查找单据，找到后勾选并输入本次核销，找不到向下滚动500px，直到上限
        :param item:传入单据数组
        """
        for height in range(0, 1000, 500):
            self.driver.execute_script("document.documentElement.scrollTop=" + str(height))
            card = self.finds(By.XPATH, AppLocator.credit_card.format(item['serial_number']))
            if len(card) > 0:  # card[0]为单号所在卡片组
                checkbox_ele = card[0].find_element(By.CSS_SELECTOR, '.check')
                check_status = checkbox_ele.get_attribute("class")
                if 'checked' not in check_status:
                    self.driver.execute_script("arguments[0].scrollIntoView(false)", card[0])
                    checkbox_ele.click()

                # 自定义等待方法(等待勾选核销单后自动带出本次核销金额，再做清空和输入操作)
                def wait_not_zero(x: WebDriver):
                    try:
                        input_ele = card[0].find_element(By.CSS_SELECTOR, 'input')
                        value_str = input_ele.get_attribute('value')
                        return value_str != "0"
                    except:
                        return False

                WebDriverWait(self.driver, 10).until(wait_not_zero)
                card[0].find_element(By.CSS_SELECTOR, 'input').clear()
                card[0].find_element(By.CSS_SELECTOR, 'input').send_keys(item['use_money'])
                card[0].find_element(By.CSS_SELECTOR, 'input').click()
                # input_ele = card[0].find_element(By.CSS_SELECTOR, 'input')
                # self.driver.execute_script('arguments[0].value=""', input_ele)
                # input_ele.send_keys(item['use_money'])
                # input_ele.click()
                break

    def up_photo(self):
        """验证上传回款单"""
        self.driver.execute_script("document.documentElement.scrollTop=600")
        self.find(By.XPATH, AppLocator.take_photo).click()
        sleep(1)
        # 借助AutoIt识别上传文件
        os.system("D:\\work\\upfile\\upfile.exe")
        uploaded_photo = self.finds(By.XPATH, AppLocator.uploaded_photo)
        return len(uploaded_photo) > 0

    def input_remark(self):
        """获取当前时间填入备注"""
        remark_time = "APP_" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.find(By.XPATH, AppLocator.remark).send_keys(remark_time)

    def submit(self):
        """提交回款单，获取单号"""
        self.find(By.XPATH, AppLocator.submit_btn).click()
        self.find(By.XPATH, AppLocator.submit_confirm_btn).click()
