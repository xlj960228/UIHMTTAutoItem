from selenium.webdriver.common.by import By

from base.base import Base



class AppBase(Base):
    """
    存储 app应用专属方法
    """
    def base_app_right_to_left(self, area_loc, find_text):
        #获取区域元素
        el = self.base_find(area_loc)
        #获取区域  位置
        location = el.location
        y = location.get("y")
        #获取元素宽高
        size = el.size
        width = size.get("width")
        height = size.get("height")

        #计算start_x start_y end_x end_y
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5

        #组合find_text包含的元素定位信息
        loc = By.XPATH, "//android.widget.HorizontalScrollView//*[contains(@text, '{}')]".format(find_text)
        #获取当前页面结构
        page_source = self.driver.page_source
        while True:

            #首先  查找一次当前页面是否存在  要找的元素
            try:
                el = self.base_find(loc, timeout=5)
                print("找到指定的频道了 ")
                el.click()
                #跳出循环
                break
            except:
                print("当前页面没有找到指定的频道元素")
                #滑动杆屏幕
                self.driver.swipe(start_x,start_y, end_x, end_y, 2000)

            if page_source == self.driver.page_source:
                print("滑不动啦, 找不到! ")
                raise Exception("异常啦! 滑到最后一屏幕也没找到")

            else:
                #更新 page_scource的值
                page_source = self.driver.page_source

    def base_app_down_to_up(self, area_loc, find_text):
        # 获取区域元素
        el = self.base_find(area_loc)
        # 获取元素宽高
        size = el.size
        width = size.get("width")
        height = size.get("height")

        # 计算start_x start_y end_x end_y
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y =  height * 0.2

        # 组合find_text包含的元素定位信息
        loc = By.XPATH, "//*[@bounds='[0,390][1080,1716]']//*[contains(@text, '{}')]".format(find_text)
        # 获取当前页面结构
        page_source = self.driver.page_source
        while True:

            # 首先  查找一次当前页面是否存在  要找的元素
            try:
                print("正在查找包含文章标题: {}".format(find_text))
                el = self.base_find(loc, timeout=5)
                print("找到 包含{} 文章的标题!  --> 文章标题为:{} ".format(find_text, el.text))
                el.click()
                # 跳出循环
                break
            except:
                print("当前页面没有找到指定的文章标题")
                # 滑动杆屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, 2000)

            if page_source == self.driver.page_source:
                print("滑不动啦, 找不到! ")
                raise Exception("异常啦! 滑到最后一屏幕也没找到")

            else:
                # 更新 page_scource的值
                page_source = self.driver.page_source



