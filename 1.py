from appium import webdriver
from page.add_user_page import Add_user_page
import page,time

class Con():
  def __init__(self):
      desired_caps = {}
      # 设备信息
      desired_caps['platformName'] = 'Android'
      # 知道确切版本时填写，不确定不填写
      # desired_caps['platformVersion'] = '4.4.4'
      # adb自动获取设备号 adb devices
      desired_caps['deviceName'] = '127.0.0.1:62005'
      # app信息,
      desired_caps['appPackage'] = 'com.android.contacts'
      desired_caps['appActivity'] = '.activities.PeopleActivity'
      # 发送中文服务端需配置两个参数，
      desired_caps['unicodeKeyboard'] = True
      desired_caps['resetKeyboard'] = True
      driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
      # driver.find_element_by_xpath().get_attribute("classname")
      self.A=Add_user_page(driver)
      self.A.click_element(page.find_u)
      self.A.click_element(page.find_XG)

  def connect_phone(self):
       data_text=self.A.get_user_data()
       print(data_text)


if __name__ == '__main__':
    con=Con()
    con.connect_phone()