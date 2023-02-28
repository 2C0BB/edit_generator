import json
from pytube import YouTube
from youtubesearchpython import VideosSearch
from moviepy import editor

MUSIC = ['tpgi.mp4', 18.0]

VID_TIME = MUSIC[1] + 10

def YTDownload(link):
    ytObject = YouTube("what is {}".format(link))
    ytObject = ytObject.streams.get_highest_resolution()
    
    try:
        ytObject.download(filename="download.mp4")
    except:
        print("Error downloading '{}'".format(link))
    
def YTSearch(term):
	videosSearch = VideosSearch('{}'.format(term), limit = 1)
    
	return videosSearch.result()["result"][0]["link"]


YTDownload(YTSearch('rubidium'))

# Perfect Girl Instrumental means the video should cut at ~18 seconds

clip = editor.VideoFileClip("download.mp4")
clip = clip.subclip(0.0, VID_TIME)

audioclip = editor.AudioFileClip("tpgi.mp4")
audioclip = audioclip.subclip(0.0, VID_TIME)

new_audioclip = editor.CompositeAudioClip([clip.audio, audioclip])
clip.audio = new_audioclip
clip.write_videofile("new_clip.mp4")