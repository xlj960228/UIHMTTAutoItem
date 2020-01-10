import sys, os
sys.path.append(os.getcwd())

import pytest
from tools.read_yaml import read_yaml


from tools.get_log import GetLog

import unittest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver

log = GetLog.get_logger()
class TestMpLogin:
    # 初始化

    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_driver(page.url_mp)
        # 获取PageMpLogin
        self.login = PageIn(self.driver).page_get_PageMpLogin()
        print("参数化读取数据为：", read_yaml("mp_login.yaml"))

    # 结束

    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 测试业务方法
    @pytest.mark.parametrize("phone, code, expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, phone, code, expect):
        # 调用登录业务方法
        self.login.page_mp_login(phone, code)
        # 断言
        try:
            assert expect == self.login.page_get_nickname()#没有指定异常信息

        except Exception as e:
            #日志
            log.error(e)
            #截图
            self.login.base_get_img()
            #抛异常
            raise
        # print("获取的昵称为: ", self.login.page_get_nickname())
        # 补货断言,抛异常
