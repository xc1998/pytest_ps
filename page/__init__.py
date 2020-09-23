# 定义元祖初始化参数，
from selenium.webdriver.common.by import By
# 搜索包
# s_b = (By.ID, "com.android.settings:id/search")
# i_b = (By.ID, "android:id/search_src_text")
# c_b = (By.XPATH, "//*[contains(@class,'android.widget.ImageButton')]")
#
# find_SS = (By.ID, "com.android.contacts:id/menu_search")
# find_user=(By.XPATH, "//*[contains(@text,'查找联系人')]")
# find_u=(By.XPATH, "//*[contains(@text,'Mr f')]")
# find_XG = (By.ID, "com.android.contacts:id/menu_edit")
# Scroll_end=(By.XPATH, "//*[contains(@text,'个人')]")
# Scroll_start=(By.XPATH, "//*[contains(@text,'电话')]")
# find_BZ=(By.XPATH, "//*[contains(@text,'备注')]")
# find_FH=(By.XPATH, "//*[contains(@class,'android.widget.ImageButton')]")

"""
添加用户
"""
add_user_el=(By.ID,"com.android.contacts:id/floating_action_button")
add_name=(By.XPATH, "//*[contains(@text,'姓名')]")
add_phone=(By.XPATH, "//*[contains(@text,'电话')]")
return_save=(By.XPATH, "//*[contains(@class,'android.widget.ImageButton')]")
get_user_list=(By.ID,"com.android.contacts:id/cliv_name_textview")
user_update = (By.ID, "com.android.contacts:id/menu_edit")

