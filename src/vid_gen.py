import yt
from constants import *
from img_vid import imgs2Vid

from moviepy import editor




def generate_video(term, music):
        
	vid_time = music[1] + 10

	yt.YTDownload(yt.YTSearch(term))

	# get downloaded video as an object and clip it to the time before the beat drop
	clip = editor.VideoFileClip(B_PATH+"download.mp4")
	clip = clip.subclip(0.0, music[1])

	# add the video of the images to the end of the clip, compose means black bars
	clip = editor.concatenate_videoclips([clip, imgs2Vid(term)], method="compose")

	# get the audio clip and clip it down so that it runs for 10s after beat drop
	audioclip = editor.AudioFileClip("tpgi.mp4")
	audioclip = audioclip.subclip(0.0, vid_time)

	# create a new audio clip which overlays the original vid audio and the edit audio
	new_audioclip = editor.CompositeAudioClip([clip.audio, audioclip])
    # set the clip's audio to the new composited audio
	clip.audio = new_audioclip

	# save the clip to a file
	clip.write_videofile(B_PATH+"new_clip.mp4", fps=24)

