import sys, os

sys.path.append(os.getcwd())
from page.Page_Obj import Page_O
from Base.Initdriver import Connect
from Base.read_data import Read_data
import pytest


def yaml_data():
    data_list = []
    data = Read_data("data").get("Search_Data")
    for i in data.keys():
        data_list.append((i, data.get(i).get("test"), data.get(i).get("expect_data")))
        print(data_list)
    return data_list


class Test_yaml():

    def setup_class(self):
        self.driver = Connect('com.android.settings', '.Settings').init_driver()
        self.po = Page_O(self.driver).re_search_page_yaml()
        self.po.click_ele()

    def teardown_class(self):
        self.po.return_clike_yaml()
        self.driver.quit()

    @pytest.mark.parametrize("test_num,text,expect_data", yaml_data())
    def test_yaml(self, test_num, text, expect_data):
        print("测试编号:%s" % test_num)
        print("预期结果:%s" % expect_data)
        self.po.input_data_yaml(text)
        self.driver.get_screenshot_as_file("./screen/%s.png" % test_num)

if __name__ == '__main__':
    pytest.main(["-s", "test_yaml.py"])
