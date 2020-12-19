#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''管理PC页面元素定位路径'''


class PCLocator:
    username = '//input[contains(@placeholder,"帐号")]'
    password = '//input[contains(@placeholder,"密码")]'
    captcha_input = '//input[@placeholder="验证码"]'
    company_input = '//input[contains(@placeholder,"请选择公司")]'
    li_span_text = '//li/span[text()="{}"]'
    login_btn = '//button[contains(@class,"login-btn-submit")]'
    login_success_msg = '//p[text()="用户登录验证通过"]'
