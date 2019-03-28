#
from PIL import Image
import sys
import os

def saveToJPG():
    if len (sys.argv) != 2 :
	print "invalid image folder path"
    	sys.exit (1)
    else:
    	imageFolderPath = str(sys.argv[1])
    	images = os.listdir(imageFolderPath)
    	count =1
    	for image in images:
    		path = imageFolderPath + "/" + image
    		img = Image.open(path)
    		imgSize=(100,100)
    		img = img.resize(imgSize)
    		imgName = "image"+str(count)+".jpg"
    		img.convert('RGB').save(imgName)
    		count = count +1
    		
    		




if __name__ == "__main__":
	saveToJPG()
