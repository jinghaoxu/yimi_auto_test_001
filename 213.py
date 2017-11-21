# from selenium import webdriver
# import time
# from selenium.webdriver.common.action_chains import ActionChains
# from pymouse import PyMouse
# from selenium.webdriver.common.keys import Keys
#
# m = PyMouse()
# m.move(0, 0)
#
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# el = driver.find_element_by_xpath('//*[@id="kw"]')
# el.send_keys('sdadad')
# el.send_keys(Keys.LEFT_CONTROL,'a')
# el.send_keys(Keys.ENTER)
# time.sleep(10)
# driver.quit()

import time
from utils import ary
driver = ary.Ary()
driver.open('https://www.baidu.com/')
driver.type('123','//*[@id="kw"]')
driver.click('//*[@id="su"]')
time.sleep(10)
driver.quit()
