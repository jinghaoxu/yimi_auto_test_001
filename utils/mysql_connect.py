"""
1. 运行sql，仅限查询
2. 创建于2017-11-09 18:50:12
3. 创建人：徐敬浩
4. 注意事项：sql查询防止注入：使用参数化
"""
import logging
import pymysql
from constants import mysqlPathConstant

mysqlPath = mysqlPathConstant.CsMysqlPath()
logger = logging.getLogger()


def mysql_select(sql):
	connection = pymysql.connect(
		host=mysqlPath.host,
		port=mysqlPath.port,
		user=mysqlPath.user,
		passwd=mysqlPath.passwd,
		db=mysqlPath.db,
		charset='utf8',
		cursorclass=pymysql.cursors.DictCursor,  # 此属性表示结果为字典类型
	)
	cursor = connection.cursor()
	data = False
	try:
		cursor.execute(sql)
		data = cursor.fetchall()
	except BaseException:
		logging.exception('数据库查询错误')
	finally:
		# connection.commit() # 此语句为提交，不提交则增删改皆不生效
		cursor.close()
		connection.close()
	print(1)
	return data


