"""
1. 创建人：徐敬浩
2. 创建时间：2017-11-14
"""
import xlrd
import data
import logging
from constants.function_list import operation_list

logger = logging.getLogger()


def rexcel():
	global col
	dataa = xlrd.open_workbook(data.EXCELDATAPATH)
	table_test = dataa.sheet_by_name('test')

	# 做校验
	if check_init(table_test):
		# 获得第一行的数据以作为键
		print(table_test.ncols)
		keys = []
		for i in range(table_test.ncols):
			keys.append(str(table_test.cell_value(0, i)))

		# dictdatas存放所有数据
		dictdatas = {}

		# dictdata存放某一行的数据
		dictdata = {}
		for row in range(1, table_test.nrows):
			for col, key in zip(range(table_test.ncols), keys):
				# 获得某一行的数据：键为第一行的数据，值为当前行的数据
				dictdata[key] = table_test.cell_value(row, col)
			# 获得所有数据，注意 = 和 copy() 的区别
			try:
				check_data(dictdata)
			except BaseException:
				logger.exception('数据错误:当前行：' + str(row) + '  当前行数据：' + str(dictdata))
				return False
			dictdatas['test_row_' + str(row)] = dictdata.copy()
		return dictdatas
	else:
		return False


# 初始验证
def check_init(excel):
	if excel.nrows < 1:
		logger.info('用例没有数据，当前行数：' + str(excel.nrows))
		return False
	elif excel.ncols != 6:
		logger.info('用例列数错误：标准列数：6，当前列数：' + str(excel.ncols))
		return False
	else:
		return True


# 验证数据
def check_data(excel):
	if excel['operation'].upper() in operation_list:
		pass
	else:
		raise BaseException('用例错误，存在错误的操作')