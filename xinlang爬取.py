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
time.sleep(3)
user_name=driver.find_element_by_id('loginName')
user_name.clear()
#输入内容
time.sleep(3)
user_name.send_keys('269383567@qq.com')
time.sleep(4)
#获取输入密码按钮框
password=driver.find_element_by_id('loginPassword')
password.clear()
time.sleep(3)
#输入密码
password.send_keys('951117hch00000')

#点击登录
time.sleep(4)
login=driver.find_element_by_id('loginAction')
login.click()
time.sleep(5)
bz=driver.find_elements_by_xpath('//h3[@class="m-text-cut"]')
bt=driver.find_elements_by_xpath('//div[@class="weibo-text"]')
time.sleep(10)
for i in range(len(bz)):
    with open("weibo.txt","a",encoding="utf-8")as f:
        f.write(str(i))
        f.write('\n')
        f.write("博主:    "+bz[i].text+"\n")
        f.write("标题:    "+bt[i].text+"\n")
        f.write("\n")
