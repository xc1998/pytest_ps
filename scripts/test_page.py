import sys, os
sys.path.append(os.getcwd())
from page.Page_Obj import Page_O
import pytest
from Base.Initdriver import Connect


class Test_page:
    def setup_class(self):
        # 实例化driver
       self.driver=Connect('com.android.settings','.Settings').init_driver()
        # 统一页面对象管理类
       self.po=Page_O(self.driver).re_search_page()
    def teardown_class(self):
        self.po.click_return()
        self.driver.quit()
    @pytest.fixture(scope="class")
    def click_ele(self):
        self.po.click_search()
    @pytest.mark.usefixtures("click_ele")
    @pytest.mark.parametrize("text", [1,2323])
    def test_search_page(self, text):
        print(text)
        self.po.search_input(text)



if __name__ == '__main__':
    pytest.main(["-s", "test_page.py"])
