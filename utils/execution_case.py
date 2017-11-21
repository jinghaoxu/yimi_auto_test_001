"""
1. 创建人：徐敬浩
2. 创建时间：2017-11-15
3. 功能：执行用例
"""
from utils import excel_wr, ary, md5cl
import logging
import time

logger = logging.getLogger()


def exe_cases():
	case_datas = excel_wr.rexcel()
	if case_datas:
		logger.info('开始执行用例')
		driver = ary.Ary()
		for data in case_datas:
			operation = case_datas[data]['operation'].upper()
			path = case_datas[data]['path']
			value = case_datas[data]['value']
			dp = case_datas[data]['dp'].upper()

			try:
				if dp:
					value = data_exe(value, dp)
				else:
					pass
				exe_case(driver=driver, operation=operation, path=path, value=value, dp=dp)
			except BaseException:
				driver.quit()
				logger.exception('执行用例失败，错误用例：行数 - ' +
				                 data.split('_')[2] +
				                 '  数据：operation:' + str(operation) +
				                 '    path:' + str(path) +
				                 '    value:' + str(value) +
				                 '    dp:' + str(dp))
				return False
		logger.info('执行用例成功')
	else:
		pass

def data_exe(value, dp):
	if dp == 'MD5':
		return md5cl.md5(value)
	else:
		return False


def exe_case(driver, operation, path, value, dp):
	# 打开网址
	if operation == 'OPEN':
		driver.open(value)

	# 最大化窗口
	elif operation == 'MAX_WINDOW':
		driver.max_window()

	# 点击一个元素
	elif operation == 'CLICK':
		driver.click(path)

	# 输入一个值
	elif operation == 'TYPE':
		if isinstance(value, float):
			if int(value) == value:
				value = int(value)
			else:
				pass
		else:
			pass
		driver.type(str(value), path)


	# 清空一个元素
	elif operation == 'CLEAR':
		driver.clear()

	# 右键一个元素
	elif operation == 'RIGHT_CLICK':
		driver.right_click(path)

	# 移动到某一个元素上
	elif operation == 'MOVE_TO_ELEMENT':
		driver.move_to_element(path)

	# 鼠标移动到一个元素上并按住
	elif operation == 'CLICK_AND_HOLD':
		driver.click_and_hold(path)

	# 双击一个元素
	elif operation == 'DOUBLE_CLICK':
		driver.double_click(path)

	# 拖动一个元素到另一个元素
	elif operation == 'DRAG_AND_DROP':
		driver.drag_and_drop()

	# 运行一段js
	elif operation == 'JS':
		driver.js(value)

	# 进入一个frame
	elif operation == 'SWITCH_TO_FRAME':
		driver.switch_to_frame(path)

	# 从一个frame出来
	elif operation == 'DRAG_AND_DROP':
		driver.switch_to_frame_out()

	# 弹窗操作
	elif operation == 'ALERT':
		if path == 'text':
			return driver.alert(path)
		else:
			driver.alert(path)

	# 等待一段时间
	elif operation == 'SLEEP':
		time.sleep(value)

	# 关闭浏览器
	elif operation == 'QUIT':
		driver.quit()

	else:
		logger.warning('错误的操作')
		raise BaseException('错误的操作')
