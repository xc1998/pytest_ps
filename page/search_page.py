from Base.Base import Base
import page


class Search_Page(Base):
    def __init__(self, driver):
        self.driver = driver

    def click_ele(self):
        self.click_element(page.s_b)

    def input_data_yaml(self,  text):
        self.input_data(page.i_b, text)

    def return_clike_yaml(self):
        self.click_element(page.c_b)

