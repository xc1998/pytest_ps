import page
import sys,os
from Base.Base import Base
sys.path.append(os.getcwd())
# 继承Base类
class Search_page(Base):
    def __init__(self,driver):
        # 初始化BASE类
        Base.__init__(self,driver)
    def click_search(self):
        # 点击搜索按钮
        self.click_element(page.s_b)

    def search_input(self, text):
        # 输入搜索内容
        self.input_data(page.i_b, text)

    def click_return(self):
        # 点击返回按钮
        self.click_element(page.c_b)

    def search_text(self, text):
        # 点击搜索按钮
        self.click_element(page.s_b)
        # 输入内容
        self.input_data(page.i_b, text)
        # 点击返回按钮
        self.click_element(page.c_b)

