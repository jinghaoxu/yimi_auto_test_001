import logging
import data
import results

# 初始化
def config_init():
	# 实例化路径
	datapath = data.DataPath()
	datapath.setcsvpath('test.csv')
	datapath.setexcelpath('test.xlsx')

	resultspath = results.ResultsPath()
	resultspath.setimgpath('img')