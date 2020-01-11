from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()
login_data = read_yaml("mp_login.yaml")[0]
class TestAppLogin:
    #初始化
    def setup_class(self):
        #获取driver
        driver = GetDriver.get_app_driver()
        #通过统一入口类获取 PageAppLogin对象
        self.app_login = PageIn(driver).page_get_PageAppLogin()


    #结束
    def teardown_class(self):
        #关闭driver
        GetDriver.quit_app_driver()

    #app登录业务方法
    def test_app_login(self, username=login_data[0], pwd=login_data[1]):
        #调用app登录业务方法
        self.app_login.page_app_login(username, pwd)
        #断言是否登录成功
        try:
            #断言
            assert self.app_login.page_if_element_exists()
        except Exception as e:
            #日志
            log.error(e)
            #截图
            self.app_login.base_get_img()
            #抛异常
            raise