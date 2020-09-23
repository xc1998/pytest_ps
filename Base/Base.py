# 显示等待导包
from selenium.webdriver.support.wait import WebDriverWait

"""
 自定义封装查找元素方法
"""


class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, loc, timeout=30, poll=0.5):
        # 定位一组元素
        return WebDriverWait(self.driver, timeout, poll) \
            .until(lambda x: x.find_elements(*loc))

    def find_element(self, loc, timeout=30, poll=0.5):
        # 定位单个元素
        """
        :param loc: 元祖类型 定位方式+属性值，类似(By.XPATH,"xpath语句") (By.ID,"id属性值")
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll) \
            .until(lambda x: x.find_element(*loc))

    # 判断元素是否存在
    def if_desp (self, loc):
        try:
            self.find_element(loc)
            return True
        except Exception as e:
            return False

    def click_element(self, loc):
        self.find_element(loc).click()

    def input_data(self, loc, text):
        input_d = self.find_element(loc)
        input_d.clear()
        input_d.send_keys(text)
