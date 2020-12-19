#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import allure
from common.app import App


@allure.feature("回款申请-预收款")
class TestReturnMoney1:
    serial_number = ""

    def setup_class(self):
        self.app = App()
        self.test_data = self.app.parse_yaml("../data/return1.yml")  # 读取测试数据
        username = self.test_data['user_apply']['username']
        password = self.test_data['user_apply']['password']
        self.main = self.app.start().login(username, password)  # 登录后返回首页对象
        self.return_page = self.main.module_page_obj("回款申报")  # 获取回款页面对象
        self.return_apply = self.main.module_apply_obj("回款申报")  # 获取回款申请页面对象

    def teardown_class(self):
        self.app.stop()

    @allure.title("登录")
    def test_01(self):
        """判断登录是否成功"""
        assert self.main.login_result()

    @allure.title("切换公司")
    def test_02(self):
        """验证切换公司是否成功"""
        company = self.test_data['company']['companyname']
        assert self.main.switch_company(company)

    @allure.title("跳转回款申报页面")
    def test_03(self):
        """验证回款申报页面标题是否与模块名称一致"""
        assert self.main.goto_module("回款申报")

    # @allure.title("跳转回款申请页面")
    # def test_04(self):
    #     """验证回款申请页面标题是否正确"""
    #     assert self.return_page.goto_apply()
    #
    # @allure.title("选择客户")
    # def test_05(self):
    #     """验证选择客户是否成功"""
    #     with allure.step("步骤1：搜索客户"):
    #         print("搜索客户")
    #     with allure.step("选择一个客户"):
    #         print("选择一个客户")
    #     assert self.return_apply.choose_customer(self.test_data['customer'])
    #
    #     # self.return_apply.goto_customer().choose_customer(self.test_data['customer'])
    #     # assert self.return_apply.customer_info() == self.test_data['customer']
    #
    # @allure.title("选择付款方式")
    # def test_06(self):
    #     """验证选择付款方式"""
    #     assert self.return_apply.choose_pay_type(self.test_data['pay_type'])
    #
    # @allure.title("选择收款银行")
    # def test_07(self):
    #     """验证选择付款方式"""
    #     assert self.return_apply.choose_bank(self.test_data['bank'])
    #
    # @allure.title("输入付款人")
    # def test_08(self):
    #     """验证输入付款人"""
    #     assert self.return_apply.input_payer(self.test_data['payer'])
    #
    # @allure.title("输入付款账号")
    # def test_09(self):
    #     """验证输入付款账号"""
    #     assert self.return_apply.input_pay_account(self.test_data['pay_account'])
    #
    # @allure.title("选择回款类型")
    # def test_10(self):
    #     """验证选择回款类型"""
    #     assert self.return_apply.choose_return_type(self.test_data['return_type'])
    #
    # @allure.title("选择产品线")
    # def test_11(self):
    #     """验证选择产品线"""
    #     if "product_line" in self.test_data:
    #         assert self.return_apply.choose_product_line(self.test_data['product_line'])
    #
    # @allure.title("选择产品")
    # def test_12(self):
    #     """验证选择产品"""
    #     if "product" in self.test_data:
    #         self.return_apply.choose_product(self.test_data['product'])
    #
    # @allure.title("新增款项")
    # def test_13(self):
    #     """验证新增款项"""
    #     assert self.return_apply.add_money(self.test_data["money_item"])
    #
    # @allure.title("查看优惠活动")
    # def test_14(self):
    #     """验证优惠活动"""
    #     if "activity" in self.test_data:
    #         assert self.return_apply.view_activity(self.test_data['activity'])
    #
    # @allure.title("上传回款单")
    # def test_15(self):
    #     """验证上传回款单"""
    #     assert self.return_apply.up_photo()
    #     self.return_apply.driver.save_screenshot("./pic/upload_photo.png")
    #     allure.attach.file("./pic/upload_photo.png", attachment_type=allure.attachment_type.PNG)
    #
    # @allure.title("验证价格政策")
    # def test_16(self):
    #     """验证价格政策(上传回款单后再验证价格政策，避免价格政策渲染过程中取到提示文字)"""
    #     assert self.return_apply.check_price_policy(self.test_data['price_policy'])
    #
    # @allure.title("填写备注")
    # def test_17(self):
    #     """获取当前时间填入备注"""
    #     self.return_apply.input_remark()
    #
    # @allure.title("提交回款单")
    # def test_18(self):
    #     """验证提交回款单,获取单据号"""
    #     self.return_apply.submit()
    # @pytest.mark.skip
    @allure.title("回款单列表查询")
    def test_19(self):
        """查找回款单,验证单据信息"""
        TestReturnMoney1.serial_number = "HKWH202012180001"
        obj = self.return_page.search(TestReturnMoney1.serial_number)
        assert obj["customer"] == self.test_data['customer']
        assert obj["money"] == self.test_data['money_sum']
        assert obj["status"] == "待确认"


@allure.feature("回款确认-预收款")
class TestReturnMoney2:

    def setup_class(self):
        self.serial_number = TestReturnMoney1.serial_number
        self.app = App()
        self.test_data = self.app.parse_yaml("../data/return1.yml")  # 读取测试数据
        username = self.test_data['user_apply']['username']
        password = self.test_data['user_apply']['password']
        self.main = self.app.start().login(username, password)  # 登录后返回首页对象
        self.return_confirm_page = self.main.module_page_obj("回款确认")  # 获取回款确认页面对象
        self.return_confirm_detail = self.main.module_detail_obj("回款确认")  # 获取回款确认详情页面对象

    def teardown_class(self):
        self.app.stop()

    @allure.title("登录")
    def test_01(self):
        """判断登录是否成功"""
        assert self.main.login_result()

    @allure.title("切换公司")
    def test_02(self):
        """验证切换公司是否成功"""
        company = self.test_data['company']['companyname']
        assert self.main.switch_company(company)

    @allure.title("跳转回款确认页面")
    def test_03(self):
        """验证回款确认页面标题是否与模块名称一致"""
        assert self.main.goto_module("回款确认")

    @allure.title("回款单列表查询")
    def test_04(self):
        """查找回款单,验证单据信息"""
        obj = self.return_confirm_page.search(self.serial_number, self.test_data['applyer'])
        assert obj["customer"] == self.test_data['customer']
        assert obj["money"] == self.test_data['money_sum']

    def test_05(self):
        """确认回款单"""
        self.return_confirm_page.goto_detail().approve()
