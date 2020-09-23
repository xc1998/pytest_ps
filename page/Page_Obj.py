import sys, os
sys.path.append(os.getcwd())
from Base.Base import Base
from page.page_search import Search_page
from page.add_page import Add_page
from page.search_page import Search_Page
from page.add_user_page import Add_user_page


class Page_O(Base):
    def __init__(self, driver):
        self.driver = driver

    # 返回搜索对象页面
    def re_search_page(self):
        return Search_page(self.driver)

    # 返回添加对象页面
    def re_add_page(self):
        return Add_page(self.driver)

    def re_search_page_yaml(self):
        return Search_Page(self.driver)

    def re_add_user_page(self):
        return Add_user_page(self.driver)
