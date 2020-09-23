"""
夜神模拟器登入模拟
  电话号码输入模拟
  1.打开通讯录
  2.点击搜索，查找方法
  3.如没有此联系人，提示沒有此人，有则修改联系人职务为总经理
  4.返回保存
"""
import pytest
from appium import webdriver
from page.Page_Obj import Page_O
from Base.Initdriver import Connect

class Test_app:
    def setup_class(self):
        self.driver=Connect('com.android.contacts','.activities.PeopleActivity').init_driver()
        self.po=Page_O(self.driver).re_add_page()
        self.po.click_SS()

    def teardown_class(self):
        self.po.click_return()
        self.driver.quit()

    @pytest.mark.parametrize("text1", ["Mr.f"])
    def test_app(self, text1):
        self.po.app_input(text1)
        self.po.click_find_user()
        self.po.click_find_XG()
        self.po.Scroll_elments()
        # self.po.add_message(text2)







if __name__ == '__main__':
    pytest.main(["-s", "test_app.py"])
