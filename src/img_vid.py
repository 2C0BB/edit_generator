from constants import *

from moviepy import editor
import wget
from youtubesearchpython import VideosSearch
import os
from PIL import Image
from moviepy.video.fx.all import crop
import bs4 as bs
import requests

# def YTImgs2Vid(term, amount):
    

# 	videosSearch = VideosSearch('{}'.format(term), limit = amount)

# 	filenames = []
    
# 	for idx, url in enumerate(videosSearch.result()["result"]):
# 		url = url["thumbnails"][0]["url"]

# 		filenames.append(download_png(url, str(idx)))

# 	clips = [editor.ImageClip(m).set_duration(1) for m in filenames]
# 	clips = [c.resize(5) for c in clips] # maybe crop here

# 	concat_clip = editor.concatenate_videoclips(clips, method="compose")
	
# 	return concat_clip

def GoogleImgs2Vid(term, amount):
	r = requests.get("https://www.bing.com/images/search?q={}".format(term), verify=False)

	if r.status_code != 200:
		raise Exception("couldn't get google images")
	
	source = r.text
	soup = bs.BeautifulSoup(source, 'html')

	imgs = soup.find_all('img')

	filt_imgs = []
	for i in imgs:
		try:
			s = imgs['src']
			if s.startswith("https://"):
				filt_imgs.append(s)
		except:
			continue

	filenames = download_list(filt_imgs)

	# concat the clips together

	clips = [editor.ImageClip(m).set_duration(1) for m in filenames]
	clips = [c.resize(5) for c in clips]

	return editor.concatenate_videoclips(clips, method="compose")



def download_list(urls):
	filenames = []

	for idx, url in enumerate(urls):
		filenames.append(download_png(url, str(idx)))

	return filenames

def download_png(url, name):
	print(url)
	#return
	file_n = wget.download(url, out=F_PATH)

	# ext = "." + file_n.split(".")[-1]
	# new_name = F_PATH + name + ext

	# if os.path.exists(new_name):
	# 	os.remove(new_name)
	# os.rename(file_n, new_name)

	im = Image.open(file_n)

	png_name = file_n.split(".")[0]+ ".png"
	im.save(png_name)

	return png_name

