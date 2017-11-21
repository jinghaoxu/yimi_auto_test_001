# 格式化json字符串
def json_gsh(data):
	res = ''
	k = 0
	data = str(data)
	for i in range(len(data)):
		ele = data[i]
		if ele == '{' or ele == '[':
			ele = ele + '\n'
			k = k + 1
			for ii in range(k):
				ele = ele + '    '
		elif ele == '}' or ele == ']':
			k = k - 1
			for ii in range(k):
				ele = "    " + ele
			ele = "\n" + ele
		elif ele == ',':
			ele = ele + '\n'
			for ii in range(k):
				ele = ele + '    '
		elif ele == ':':
			ele = ele + ' '
		res = res + ele
	return res