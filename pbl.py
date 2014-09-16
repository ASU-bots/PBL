"""
The Python Botting Library
"""

import time
import autopy as ap
#from PIL import ImageGrab
import pyscreenshot as ImageGrab
import os.path
import numpy as np

from multiprocessing import Process
class screen_grab:
	def __init__(self):
		self.t1=time.clock()

	def get_screen_area(self, function, fps):
		"""Grabs a portion of the screen and sends it to function at fps rate.

		Args:
			function (function): a function this function will call every 1/fps seconds.
			fps (int): number of times per second this function will execute.
		"""
		
		try:
			input('move mouse to top left corner, then press enter.')
		except SyntaxError, NameError:
			pass
		tl=(ap.mouse.get_pos())
		try:
			input('move mouse to bottom right corner, then press enter.')
		except SyntaxError, NameError:
			pass
		br=(ap.mouse.get_pos())
		#make br position added to tl instead of absolute position
		#br=(br[0]-tl[0]),(br[1]-tl[1])
		box=(tl[0],tl[1],br[0],br[1])

		while(self.running):

			#limit max loop rate to frame rate
			self.t2=time.clock()
			time_allapsed=self.t2-self.t1
			if time_allapsed > 1/fps:
				time_allapsed=1/fps
			time.sleep(1/fps - time_allapsed)
			self.t1=time.clock()

			bmp=ImageGrab.grab(box)
			#the following is courtesy of http://stackoverflow.com/a/24213099
			cvImage= np.array(bmp.getdata(),dtype=uint8).reshape((bmp.size[1],bmp.size[0]),3)
			function(frame=cvImage)

			


#__all__=[]

def get_screen_object(name,times=1):
	"""
	Grabs a portion of the screen and outputs it to a file under bmp/name<number>.bmp

	Args:
		name (string): a name to give the set of images
		times (int): number of images to take

	Returns:
		List: Empty if failed, filename strings if succeeded.

	Raises:
		
	"""
	
	file_list=[]

	for i in xrange(times):
		
		try:
			input('move mouse to top left corner, then press enter.')
		except SyntaxError, NameError:
			pass
		tl=(ap.mouse.get_pos())
		try:
			input('move mouse to bottom right corner, then press enter.')
		except SyntaxError, NameError:
			pass
		br=(ap.mouse.get_pos())
		#make br position added to tl instead of absolute position
		#br=(br[0]-tl[0]),(br[1]-tl[1])
		box=(tl[0],tl[1],br[0],br[1])
		print box
		bmp=ImageGrab.grab(box)
		

		try:
			filename="bmp/"+str(name)+str(i)+".bmp"
			while os.path.isfile(filename):
				filename="bmp/"+str(name)+str(i)+".bmp"
				i+=1
			bmp.save(filename, "BMP")
			file_list.append(filename)
		except IOError:
			print "Error: bmp directory does not exist"
		except SystemError:
			print "Error: bmp size <=0"

	return file_list

if __name__=="__main__":
	get_screen_object("test",6)
