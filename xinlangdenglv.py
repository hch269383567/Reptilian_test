
import time

from selenium.webdriver.common.by import By

from selenium import webdriver


driver = webdriver.Chrome()

driver.set_window_size(1366, 768)

driver.set_page_load_timeout(20)

driver.set_script_timeout(10)

driver.get('https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 20 秒是最长等待时间，  0.5 秒是间隔轮询时间

# 绝对等待
time.sleep(10)

username = driver.find_element_by_id('loginName')
# input 输入标签，在输入内容之前，一定要先 clear
username.clear()
# 输入 内容
username.send_keys('214414266@qq.com')


# 输入 密码
password = driver.find_element_by_id('loginPassword')
# input 输入标签，在输入内容之前，一定要先 clear
password.clear()
# 输入 内容
password.send_keys('a.2cnxin')


# 点击 登录
login_submit = driver.find_element_by_id('loginAction')
login_submit.click()

time.sleep(5)

message = driver.find_element_by_class_name('lite-iconf.lite-iconf-msg')
message.click()

time.sleep(5)
driver.quit()


