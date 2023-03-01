from constants import *

from pytube import YouTube
from youtubesearchpython import VideosSearch

def YTDownload(link):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_highest_resolution()
    
    try:
        ytObject.download(filename = B_PATH+"download.mp4")
    except:
        print("Error downloading '{}'".format(link))


def YTSearch(term):
	videosSearch = VideosSearch('{}'.format(term), limit = 1)
    
	return videosSearch.result()["result"][0]["link"]