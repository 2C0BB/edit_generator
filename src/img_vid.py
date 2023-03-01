from constants import *

from moviepy import editor
import wget
from youtubesearchpython import VideosSearch
import os
import glob
from PIL import Image

def imgs2Vid(term):
    

	videosSearch = VideosSearch('{}'.format(term), limit = 5)

	filenames = []
    
	for idx, url in enumerate(videosSearch.result()["result"]):
		url = url["thumbnails"][0]["url"]

		filenames.append(download_png(url, str(idx)))
              
	#filenames  = ["./frames/"+x for x in filenames]

	clips = [editor.ImageClip(m).set_duration(1) for m in filenames]

	concat_clip = editor.concatenate_videoclips(clips, method="compose")
	
	return concat_clip
	#concat_clip.write_videofile("test.mp4", fps=24)


def download_png(url, name):
	file_n = wget.download(url, out=F_PATH)

	ext = "." + file_n.split(".")[-1]
	new_name = F_PATH + name + ext

	if os.path.exists(new_name):
		os.remove(new_name)
	os.rename(file_n, new_name)

	im = Image.open(new_name)

	png_name = F_PATH + name + ".png"
	im.save(png_name)

	return png_name

