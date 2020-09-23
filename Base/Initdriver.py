from appium import webdriver

class Connect:
   def __init__(self,appPackage,appActivity):
           self.appPackage=appPackage
           self.appActivity=appActivity
   def init_driver(self):
        desired_caps = {}
        # 设备信息
        desired_caps['platformName'] = 'Android'
        # 知道确切版本时填写，不确定不填写
        # desired_caps['platformVersion'] = '4.4.4'
        # adb自动获取设备号 adb devices
        desired_caps['deviceName'] = '127.0.0.1:62025'
        # 重置应用状态
        desired_caps['noReset'] = 'true'
        # app信息
        desired_caps['appPackage'] = self.appPackage
        desired_caps['appActivity'] = self.appActivity
        # 发送中文服务端需配置两个参数，
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return driver


