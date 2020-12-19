#!/usr/bin/env python
# -*- coding:utf-8 -*-
import allure
import pytest
from common.pc import PC


class TestDemo:
    def setup_class(self):
        self.pc = PC()
        test_data = self.pc.parse_yaml("../data/return1.yml")  # 读取测试数据
        username = test_data['user_admin']['username']
        password = test_data['user_admin']['password']
        company = test_data['company']['companyname']
        self.main = self.pc.start().login(username, password, company)

    @allure.title("登录")
    def test_01(self):
        """判断登录是否成功"""
        login_result = self.main.login_result()
        assert login_result
