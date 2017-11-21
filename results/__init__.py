import os

IMGDATAPATH = os.path.dirname(__file__) + '\\img'


class ResultsPath(object):
	def __init__(self):
		self.DATAPATH = os.path.dirname(__file__)
		self.IMGDATAPATH = ''

	def setimgpath(self, path):
		global IMGDATAPATH
		self.IMGDATAPATH = self.DATAPATH + '\\' + path

	def getimgpath(self):
		return self.IMGDATAPATH
