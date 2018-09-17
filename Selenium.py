from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


# 登录
def login(un, pwd):

   # 输入用户名和密码
    WebDriverWait(browser, 1).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login-form"]/div[1]/div/input'))
    ).send_keys(un)
    WebDriverWait(browser, 1).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login-form"]/div[2]/div/input'))
    ).send_keys(pwd)
    time.sleep(1)
    # 登录
    WebDriverWait(browser, 1).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login-form"]/div[3]/div[1]/button'))
    ).click()
    # 等待网页跳转
    time.sleep(5)





# 主函数
def main(un, pwd):
    while 1:
        return1 = os.system('ping www.baidu.com -c 2')
        if return1:
            print('ping fail')
            path = "/home/pi/geckodriver"
            global browser
            browser = webdriver.Firefox(executable_path=path)
            browser.get('http://8.8.8.8')
            login(un, pwd)
            browser.quit()

        else:
            print('ping ok')



username = 'username'
password = 'password'
main(username, password)
