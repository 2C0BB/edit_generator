import json
from pytube import YouTube
from youtubesearchpython import VideosSearch

def YTDownload(link):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_highest_resolution()
    
    try:
        ytObject.download()
    except Exception as e:
        print("Error downloading '{}\n{}'".format(link, e.message))
    
def YTSearch(term):
	videosSearch = VideosSearch('what is {}'.format(term), limit = 1)
        
	return videosSearch.result()["result"][0]["link"]


YTDownload(YTSearch('francium'))

