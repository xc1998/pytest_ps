import page
import sys,os
from Base.Base import Base
sys.path.append(os.getcwd())

class Add_page(Base):
    def __init__(self,driver):
        # 初始化BASE类
        Base.__init__(self,driver)
    # 点击搜索
    def click_SS(self):
        self.click_element(page.find_SS)
    # 输入查询内容
    def app_input(self, text):
        # 输入搜索内容
        self.input_data(page.find_user, text)
    # 点击查询到的对象
    def click_find_user(self):
        self.click_element(page.find_u)
    # 点击修改对象
    def click_find_XG(self):
        self.click_element(page.find_XG)
    # 滑动添加备注信息
    # def Scroll_elments(self):
    #     el_list=self.find_elements(page.Scroll_end,page.Scroll_start)
    #     list_E={}
    #     for i in el_list:
    #       list_E.append(i)
    #     self.Scrool_element(list_E.,el2)
    def add_message(self,text):
        self.input_data(page.find_BZ,text)
    def click_return(self):
        # 点击返回按钮
        self.click_element(page.find_FH)

    def change_Number(self, text1,text2):
        self.click_element(page.find_TXL)
        self.click_element(page.find_SS)
        self.input_data(page.find_user, text1)
        self.click_element(page.find_u)
        self.click_element(page.find_XG)
        el1=self.find_element(page.Scroll_end)
        el2=self.find_element(page.Scroll_start)
        self.Scrool_element(el1,el2)
        self.input_data(page.find_BZ, text2)
        self.click_element(page.find_FH)