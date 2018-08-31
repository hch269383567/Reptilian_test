
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
#初始化浏览器
driver=webdriver.Firefox()
#设置窗口大小
driver.set_window_size(1366,768)
#设置页面加载超时时间
driver.set_page_load_timeout(10)
#设置脚本超时时间
driver.set_script_timeout(10)







#目标网址
driver.get('https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

#获取输入用户名按钮框
time.sleep(1)
user_name=driver.find_element_by_id('loginName')
user_name.clear()
#输入内容
time.sleep(1)
user_name.send_keys('269383567@qq.com')
# time.sleep(1)
#获取输入密码按钮框
password=driver.find_element_by_id('loginPassword')
password.clear()
# time.sleep(2)
#输入密码
password.send_keys('951117hch00000')

#点击登录
time.sleep(2)
login=driver.find_element_by_id('loginAction')
login.click()
time.sleep(4)

message = driver.find_element_by_class_name('lite-iconf.lite-iconf-msg')
message.click()


time.sleep(2)
ms=driver.find_elements_by_class_name('m-text-cut')[4]
ms.click()
time.sleep(3)
#获取文本
ww=driver.find_element_by_class_name("box-left")[0].click()

wz=driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/div/div[1]/textarea[1]').click()
# wz.clear()
# wz.click()
wz.send_keys('我是谁，在哪里')



# #点击表情按钮
ss=driver.find_element_by_xpath('//span[@class="lite-iconf lite-iconf-emote"]')
ss.click()


time.sleep(2)
#获取拜拜表情
bq=driver.find_element_by_class_name('face_wrapper.face.face-dbaibai')
bq.click()

time.sleep(2)
#发送
fs=driver.find_element_by_class_name("btn-send")
fs.click()


