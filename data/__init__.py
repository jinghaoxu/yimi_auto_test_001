import os

global CSVDATAPATH
global EXCELDATAPATH


class DataPath(object):
	def __init__(self):
		self.DATAPATH = os.path.dirname(__file__)
		self.CSVDATAPATH = ''
		self.EXCELDATAPATH = ''

	def setcsvpath(self, path):
		global CSVDATAPATH
		CSVDATAPATH = self.DATAPATH + '\\' + path

	def setexcelpath(self, path):
		global EXCELDATAPATH
		EXCELDATAPATH = self.DATAPATH + '\\' + path

	def getcsvpath(self):
		return self.CSVDATAPATH

	def getexcelpath(self):
		return self.EXCELDATAPATH

