import sys, os
sys.path.append(os.getcwd())
from page.Page_Obj import Page_O
from Base.Initdriver import Connect
from Base.read_data import Read_data
import pytest, allure

def read_test_data():
    list_data = []
    test_Data = Read_data("data").get("User")
    for i in test_Data.keys():
        list_data.append((i, test_Data.get(i).get("name")
                          , test_Data.get(i).get("phone"),
                          test_Data.get(i).get("expect")))
    return list_data


class Test_add_user:
    def setup_class(self):
        self.driver = Connect('com.android.contacts', '.activities.PeopleActivity').init_driver()
        self.add_user_obj = Page_O(self.driver).re_add_user_page()

    def teardown_class(self):
        self.driver.quit()

    @allure.step(title="点击新建联系人")
    @pytest.fixture
    def add_user(self):
        self.add_user_obj.click_find_user()

    @pytest.mark.parametrize("test_num,name,phone,expect", read_test_data())
    @pytest.mark.usefixtures("add_user")
    def test_add_user(self, test_num, name, phone, expect):
        self.add_user_obj .add_user_data(name, phone)
        if test_num == "test_001":
            assert expect not in self.add_user_obj .get_user_list()
        else:
            assert expect in self.add_user_obj .get_user_list()


if __name__ == '__main__':
    pytest.main(["-s", "test_add_user.py"])
