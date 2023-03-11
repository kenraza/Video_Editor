from pytube import YouTube
from pytube import YouTube
from moviepy.editor import *
import json, os, time
from requests import get
import os


youtube_video = []

f = open('list_scenes.json')

scenes = json.load(f)

for scene in scenes['list_scenes']:
    url = scene["scene"]
    youtube_video.append(url)

f.close()


# Donwload Youtube Videos
def download_youtube_videos():
    i = 1
    for video in youtube_video:
        yt = YouTube(video)
        vid = yt.streams.filter(file_extension="mp4").get_by_resolution("720p").download()
        os.rename(vid, f"scenes/scene{i}.mp4")
        i += 1

#Edit The Videos
#.subclip(60, 70) python will delete any portion of video before 60 secs and after 70 secs
#this will leave you with a 10 sec video. the video duration should always be in secs. 
def edit_videos():
    l_files = os.listdir("scenes")
    for file in l_files:
        clip1 = VideoFileClip(f"scenes/scene1.mp4").subclip(, ).fx( vfx.colorx, 1.0) #In seconds specify the clip that needs to be cut out of video downloaded
        clip2 = VideoFileClip(f"scenes/scene2.mp4").subclip(, ).fx( vfx.colorx, 1.0)
        clip3 = VideoFileClip(f"scenes/scene3.mp4").subclip(, ).fx( vfx.colorx, 1.0)
        clips = (clip1, clip2, clip3)
        
        
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("final_video.mp4")
        

    


if __name__ == "__main__":
    download_youtube_videos()
    edit_videos()

