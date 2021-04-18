# 自动打卡  厦门大学  每日健康打卡
# encoding=utf-8 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入鼠标
from selenium.webdriver.common.keys import Keys #引入键盘
import time

 # 打开网址登陆
driver = webdriver.Edge(
    'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe'
)
url = "https://ids.xmu.edu.cn/authserver/login?service=https://xmuxg.xmu.edu.cn/login/cas/xmu"
driver.get(url)
 # 找到输入框并输入查询内容
elem = driver.find_element_by_id("username")
elem.send_keys("你的学号")
elem = driver.find_element_by_id("password")
elem.send_keys("你的密码")
 # 提交表单
driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[4]/button').click()

print('登录成功！')
url = "https://xmuxg.xmu.edu.cn/app/214"
driver.get(url)
#我的表单
driver.find_element_by_xpath('//*[@id="mainM"]/div/div/div/div[1]/div[2]/div/div[3]/div[2]').click()
#xpath 定位然后使用键盘向下按键进行滚动
time.sleep(1)
driver.find_element_by_xpath('//*[@id="select_1582538939790"]/div/div').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[8]/ul/div').click()
 # 提交
time.sleep(3)
driver.find_element_by_class_name("form-save position-absolute").click()
driver.switch_to_alert()
time.sleep(2)
print('打卡成功')
  # 退出
driver.close()