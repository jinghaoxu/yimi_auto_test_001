"""
1. 创建人：徐敬浩
2. 创建时间：2017-11-14
3. 目前有问题，暂时不用
"""

import csv
import data
import logging
logger = logging.getLogger()

# 读取配置文件里面的数据，以第一行为键，返回字典数据
def rcsv():
	with open(data.CSVDATAPATH, 'r') as f:
		reader = csv.DictReader(f)
		dictdata = {}
		print(reader.line_num)
		for i in reader:
			for j in i:
				dictdata[j] = i[j]
	print(dictdata)
	return dictdata

def testing_csv():
	csvdata = rcsv()
	print(csvdata)
	if csvdata.__len__() == 0:
		logger.warning('测试用例里面没有数据')
	elif None in csvdata.keys():
		print(csvdata[None])
		logger.warning('列数超标了哦')
	else:
		print(1)