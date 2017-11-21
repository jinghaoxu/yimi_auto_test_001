"""
1. 操作host文件
2. 判断、修改
"""
from constants import hostPath
import logging
import socket

logger = logging.getLogger()


# 读取host文件
def host_read():
	with open('C:\Windows\System32\drivers\etc\hosts', 'r', encoding='UTF-8') as fdr:
		fdrr = fdr.read()
	return fdrr


# 更新host:枚举值：stage1(预发布1)，stage2(预发布2)，prod(正式)
def up_host(path='stage1'):
	if path == 'stage1':
		host_data = hostPath.HOST_YU_01
	elif path == 'stage2':
		host_data = hostPath.HOST_YU_02
	else:
		host_data = ''
		path = 'prod'
	logger.info('host开始更新： ' + path)

	with open('C:\Windows\System32\drivers\etc\hosts', 'w+', encoding='UTF-8') as fdr:
		fdr.writelines(host_data)
	if path == judge_now_host():
		logger.info('host更新成功： ' + path)
	else:
		logger.error('host更新失败： ' + path)
		raise BaseException('host更新失败： ' + path + '   可能是WIFI错误')


# 判断当前环境
def judge_now_host():
	try:
		ip = socket.gethostbyname(hostPath.IP_URL)
		if ip == hostPath.HOST_YU_01_IP:
			return 'stage1'
		elif ip == hostPath.HOST_YU_02_IP:
			return 'stage2'
		else:
			return 'prod'
	except BaseException:
		logger.exception('Error:判断host环境失败')


if __name__ == '__main__':
	print(judge_now_host())
