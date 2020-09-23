import sys, os

sys.path.append(os.getcwd())
from Base.Base import Base
import page
import allure, time


class Add_user_page(Base):
    def __init__(self, driver):
        self.driver = driver

    # "点击添加按钮"
    def click_find_user(self):
        self.click_element(page.add_user_el)

    # 返回保存
    def click_return_button(self):
        self.click_element(page.return_save)

    # 得到用户名列表
    def get_user_list(self):
        user_list = self.find_elements(page.get_user_list)
        return [i.text for i in user_list]

    # 添加联系人
    def add_user_data(self, name, phone):
        allure.attach("描述", "点击添加用户名")
        self.input_data(page.add_name, name)
        allure.attach("描述", "点击添加手机号")
        self.input_data(page.add_phone, phone)
        allure.attach("描述", "点击返回保存")
        self.click_return_button()
        # 判断是否在用户详情页
        if self.if_desp(page.user_update):
            allure.attach("描述", "点击手机返回按钮")
            self.driver.keyevent(4)
