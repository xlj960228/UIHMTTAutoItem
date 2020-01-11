from time import sleep

from page.page_in import PageIn
from tools.get_driver import GetDriver


class TestAppAricle:
    #初始化
    def setup_class(self):
        sleep(5)
        #获取driver
        driver = GetDriver.get_app_driver()
        #通过统一入口类 对象
        self.page_in = PageIn(driver)
        #调用登陆成功依赖方法(需要在PageAppLogin新增次方法)
        self.page_in.page_get_PageAppLogin().page_app_login_success()
        #获取PageAppArticle对象
        self.article = self.page_in.page_get_PageAppArtile()

    #结束
    def teardown_class(self):
        #关闭发river
        GetDriver.quit_app_driver()

    #查找文章测试方法
    def test_app_article(self):
        #调用查找文章方法
        self.article.page_app_article(find_text="后端", title_text="java")