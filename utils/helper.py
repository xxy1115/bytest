#!/usr/bin/python
# -*- coding: utf-8 -*-

import base64

from Crypto.Cipher import AES


# 帮助工具类
class Helper:

    @staticmethod
    def parse_captcha(content, aes_secret_key='1v5gQ+D8bBKT1mbLRo+6Ew=='):
        # 设置加密模式为ECB
        mode = AES.MODE_ECB
        # padding算法
        unpad = lambda s: s[0:-ord(s[-1:])]
        # 内容解码
        decode_content = base64.b64decode(content)
        # 秘钥解码
        decode_aes_secret_key = base64.b64decode(aes_secret_key)
        # 初始化解密器
        cryptor = AES.new(decode_aes_secret_key, mode)
        # 执行解密
        plain_text = cryptor.decrypt(decode_content)
        # 删除填充
        return unpad(plain_text).decode('utf-8')
