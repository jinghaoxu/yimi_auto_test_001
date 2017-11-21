from PIL import ImageGrab
import results
import time

def screen():
	im = ImageGrab.grab()
	im.save(results.IMGDATAPATH + '\\' + str(time.time())+'.png')

if __name__ == '__main__':
	print(time.time())