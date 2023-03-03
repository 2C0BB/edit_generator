import yt
from constants import *
from img_vid import GoogleImgs2Vid

from moviepy import editor
from moviepy.video.fx.all import crop



def generate_video(vid_term, img_term, music):
        
	vid_time = 23.0

	yt.YTDownload(yt.YTSearch(vid_term))

	# get downloaded video as an object and clip it to the time before the beat drop
	clip = editor.VideoFileClip(B_PATH+"download.mp4")
	clip = clip.subclip(0.0, 15.0)
	#clip = crop(clip, x1=100, width=1080)
	clip = clip.resize(2)

	# add the video of the images to the end of the clip, compose means black bars
	clip = editor.concatenate_videoclips([clip, GoogleImgs2Vid(img_term, 8)], method="compose")

	# get the audio clip and clip it down so that it runs for 10s after beat drop
	audioclip = editor.AudioFileClip(music)

	# create a new audio clip which overlays the original vid audio and the edit audio
	new_audioclip = editor.CompositeAudioClip([clip.audio, audioclip])
    # set the clip's audio to the new composited audio
	clip.audio = new_audioclip

	# save the clip to the output folder as "new_clip.mp4"
	clip.write_videofile(B_PATH+"new_clip.mp4", fps=24)

