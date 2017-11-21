import logging
from logging import handlers
import os

BASEFILEPATH = os.path.dirname(__file__)

# 设置一个基本的logger
logger = logging.getLogger()

# 设置log等级
logger.setLevel(logging.DEBUG)

# 设置一个log文件
timefilehandler_info = handlers.TimedRotatingFileHandler(BASEFILEPATH + '/ary_info.log', 'D', 1, 0)
timefilehandler_info.setLevel(logging.INFO)
timefilehandler_debug = handlers.TimedRotatingFileHandler(BASEFILEPATH + '/ary_debug.log', 'D', 1, 0)
timefilehandler_debug.setLevel(logging.DEBUG)
timefilehandler_error = handlers.TimedRotatingFileHandler(BASEFILEPATH + '/ary_error.log', 'D', 1, 0)
timefilehandler_error.setLevel(logging.ERROR)

timefilehandler_debug.suffix =  "%Y%m%d-%H%M.log"
timefilehandler_info.suffix = "%Y%m%d-%H%M.log"
timefilehandler_error.suffix = "%Y%m%d-%H%M.log"

# 创建一个控制台流
streamhandler = logging.StreamHandler()
streamhandler.setLevel(logging.INFO)

# 设置消息的格式，文件应用格式
formatter = logging.Formatter(
	"%(asctime)s - %(name)s - %(filename)s[line:%(lineno)d] - %(levelname)s >>> %(message)s")
timefilehandler_info.setFormatter(formatter)
timefilehandler_debug.setFormatter(formatter)
timefilehandler_error.setFormatter(formatter)
streamhandler.setFormatter(formatter)

# logger填充到log文件里面和控制台
logger.addHandler(timefilehandler_info)
logger.addHandler(streamhandler)
logger.addHandler(timefilehandler_debug)
logger.addHandler(timefilehandler_error)
