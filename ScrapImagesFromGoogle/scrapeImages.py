# usage :
#   
# python scrapeImages.py --search "rose flower" --num_images 10 --directory "<path/to/your/destination/folder>" 
#
#......................................................
from bs4 import BeautifulSoup
import requests
import re
import urllib2
import os
import argparse
import sys
import json

# adapted from http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def main(args):
	parser = argparse.ArgumentParser(description='Scrape Google images')
	parser.add_argument('-s', '--search', default='bananas', type=str, help='search term')
	parser.add_argument('-n', '--num_images', default=10, type=int, help='num images to save')
	parser.add_argument('-d', '--directory', default='/Users/gene/Downloads/', type=str, help='save directory')
	args = parser.parse_args()
	query = args.search#raw_input(args.search)
	max_images = args.num_images
	save_directory = args.directory
	image_type="Action"
	query= query.split()
	query='+'.join(query)
	url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
	header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
	soup = get_soup(url,header)
	ActualImages=[]# contains the link for Large original images, type of  image
	for a in soup.find_all("div",{"class":"rg_meta"}):
	    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
	    ActualImages.append((link,Type))
	count =0
	for i , (img , Type) in enumerate( ActualImages):
	    if count == 50 :
		break
	    try:
	        req = urllib2.Request(img, headers={'User-Agent' : header})
	        raw_img = urllib2.urlopen(req).read()
		if Type == "jpg" :
	        	if len(Type)==0:
	        	    f = open(os.path.join(save_directory , "img" + "_"+ str(i)+".jpg"), 'wb')
			    #f.write(raw_img)
                	    #f.close() 
	        	else :
	        	    f = open(os.path.join(save_directory , "img" + "_"+ str(i)+"."+Type), 'wb')
			    print str(len(Type)) + Type
			    #f.close()
		        f.write(raw_img)
		        f.close()
			count = count +1
	    except Exception as e:
	        print "could not load : "+img
	        print e

if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
