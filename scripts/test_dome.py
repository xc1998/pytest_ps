from selenium.webdriver.common.by import By
from Base.Base import Base
from appium import webdriver
import pytest
class Test_Dome:
    def setup(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        # 知道确切版本时填写，不确定不填写
        # desired_caps['platformVersion'] = '4.4.4'
        # adb自动获取设备号 adb devices
        desired_caps['deviceName'] = '127.0.0.1:62005'
        # app信息
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        # 发送中文服务端需配置两个参数，
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.base_data=Base(self.driver)
    def teardown(self):
        self.driver.quit()
        print("测试结束")
    def test_a(self):
        s_b={By.ID,"com.android.settings:id/search"}
        i_b={By.ID,"android:id/search_src_text"}
        self.base_data.click_element(s_b)
        self.base_data.input_data(i_b,"afbdd")

if __name__ == '__main__':
    pytest.main(["-s","test_dome.py"])

