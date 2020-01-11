from page.page_app_article import PageAppArtile
from page.page_app_login import PageAppLogin
from page.page_mis_audit import PageMisAudit
from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class PageIn:

    def __init__(self, driver):
        self.driver = driver


    #获取自媒体自动登录对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    #获取自媒体登录页面对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    #获取PageMisLogin对象
    def page_get_PageMisLogin(self):
        return PageMisLogin(self.driver)

    #获取PageMisAudit对象
    def page_get_PageMisAudit(self):
        return PageMisAudit(self.driver)


    #获取PageAppLogin对象
    def page_get_PageAppLogin(self):
        return PageAppLogin(self.driver)

    #获取PageAppArticle对象
    def page_get_PageAppArtile(self):
        return PageAppArtile(self.driver)