"""
1. selenium浏览器各种操作
2. 创建人：徐敬浩
3. 创建时间：2017-11-11
"""
from selenium import webdriver
import datetime
import time
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse

logger = logging.getLogger()
m = PyMouse()


class Ary(object):
	def __init__(self, browser='chrome'):
		logger.info('开始打开chrome浏览器')
		if browser.upper() == 'CHROME':
			driver = webdriver.Chrome()
		else:
			driver = False
		try:
			self.driver = driver
			self.url = driver.current_url
			logger.info('打开浏览器成功')
		except:
			logger.exception('打开浏览器错误')

	def element_wait(self, xpath):
		WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

	def get_element(self, xpath, css="path"):

		if css == "path":
			element = self.driver.find_element_by_xpath(xpath)
		else:
			element = self.driver.find_elements_by_partial_link_text(xpath)
		return element

	def get_elements(self, xpath, css="path"):

		if css == "path":
			elements = self.driver.find_elements_by_xpath(xpath)
		else:
			elements = self.driver.find_elements_by_partial_link_text(xpath)
		return elements

	def open(self, url='http://mis.1mifudao.com/'):
		"""
		1.打开一个网址
		2.例子： driver.open("https://www.baidu.com")
		"""
		if 'http' in url:  # driver.open("http://192.168.1.222:8008")
			pass
		elif '192' in url:  # driver.open("192.168.1.222:8008")
			url = 'http://' + url
		elif '8' in url:  # driver.open("8008")
			url = 'http://192.168.1.223:' + url
		else:  # driver.open('mis.1mifudao')
			url = 'http://' + url + '.com'
		self.driver.maximize_window()
		self.driver.get(url)
		time.sleep(0.5)

	def max_window(self):
		"""
		1.使当前窗口最大化
		2.例子： driver.max_window()
		"""
		self.driver.maximize_window()

	def type(self, text, xpath):
		"""
		1.在一个元素里输入字符
		2.例子： driver.type("sss",".//*[@id='kw']")
		"""
		self.element_wait(xpath)
		self.get_element(xpath).send_keys(text)

	def clear(self, xpath):
		"""
		1.将一个元素清空
		2.例子：driver.clear(".//*[@id='kw']")
		"""
		self.element_wait(xpath)
		self.get_element(xpath).clear()

	def click(self, xpath):
		"""
		1.点击一个元素
		2.例子：driver.click(".//*[@id='su']")
		"""
		self.element_wait(xpath)
		el = self.get_element(xpath)
		a = 0
		while a < 10:
			try:
				self.get_element(xpath).click()
				break
			except:
				time.sleep(0.5)
				a += 1

	def right_click(self, xpath):
		"""
		1.右键点击一个元素
		2.例子：driver.right_click(".//*[@id='su']")
		"""
		self.element_wait(xpath)
		el = self.get_element(xpath)
		ActionChains(self.driver).context_click(el).perform()

	def move_to_element(self, xpath):
		"""
		1.鼠标移动到一个元素上
		2.例子：driver.move_to_element(".//*[@id='su']")
		"""
		self.element_wait(xpath)
		el = self.get_element(xpath)
		m.move(0, 0)
		ActionChains(self.driver).move_to_element(el).perform()

	def click_and_hold(self, xpath):
		"""
		1.鼠标移动到一个元素上按住
		2.例子：driver.move_to_element(".//*[@id='su']")
		"""
		self.element_wait(xpath)
		el = self.get_element(xpath)
		m.move(0, 0)
		ActionChains(self.driver).click_and_hold(el).perform()

	def double_click(self, xpath):
		"""
		1.双击一个元素
		2.例子：driver.double_click(".//*[@id='su']")
		"""
		self.element_wait(xpath)
		el = self.get_element(xpath)
		ActionChains(self.driver).double_click(el).perform()

	def drag_and_drop(self, star, over):
		"""
		1.拖动一个元素到另一个元素
		2.例子：driver.drag_and_drop(".//*[@id='su']",".//*[@id='kw']")
		"""
		self.element_wait(star)
		el = self.get_element(star)
		self.element_wait(over)
		tar = self.get_element(over)
		m.move(0, 0)
		ActionChains(self.driver).drag_and_drop(el, tar).perform()

	def quit(self):
		"""
		1.关闭浏览器
		2.driver.quit()
		"""
		self.driver.quit()

	def js(self, script):
		"""
		1.执行js语句
		2.driver.js(js)
		"""
		self.driver.execute_script(script)
		time.sleep(0.5)

	def attr(self, xpath, attr):
		"""
		1.返回相应元素的某种属性
		2.driver.attr(".//p",text)
		"""
		self.element_wait(xpath)
		el = self.get_element(xpath)
		time.sleep(0.1)
		return xpath.get_attribute(attr)

	def key(self, xpath, key):
		self.element_wait(xpath)
		el = self.get_element(xpath)
		time.sleep(0.1)
		el.send_keys(key)

	def pop_up(self):
		"""
		1.返回mis弹窗的内容
		2.print driver.pop_up()
		"""
		pop = self.driver.find_element_by_xpath(".//div[@class='handle_text']/p")
		return pop[5].text

	def switch_to_frame(self, xpath, index=0):
		self.element_wait(xpath)
		el = self.get_elements(xpath)
		self.driver.switch_to.frame(el[index])

	def switch_to_frame_out(self):
		self.driver.switch_to.default_content()

	def alert(self, common="text"):
		try:
			al = Alert(self.driver)
		except:
			time.sleep(0.5)
			al = Alert(self.driver)
		if common == "text":
			return al.text
		elif common == "accept":
			Alert(self.driver).accept()
		elif common == 'dismiss':
			Alert(self.driver).dismiss()
		else:
			pass

	def page_list(self, url=''):
		text = self.get_element(url)
