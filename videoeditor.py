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
def edit_videos():
    l_files = os.listdir("scenes")
    for file in l_files:
        clip1 = VideoFileClip(f"scenes/scene1.mp4").subclip(78, 81).fx( vfx.colorx, 1.0)
        clip2 = VideoFileClip(f"scenes/scene2.mp4").subclip(23, 25).fx( vfx.colorx, 1.0)
        clip3 = VideoFileClip(f"scenes/scene3.mp4").subclip(146, 157).fx( vfx.colorx, 1.0)
        clip4 = VideoFileClip(f"scenes/scene4.mp4").subclip(67, 70).fx( vfx.colorx, 1.0)
        clip5 = VideoFileClip(f"scenes/scene5.mp4").subclip(100, 104).fx( vfx.colorx, 1.0)
        clip6 = VideoFileClip(f"scenes/scene6.mp4").subclip(59, 62).fx( vfx.colorx, 1.0)
        clip7 = VideoFileClip(f"scenes/scene7.mp4").subclip(164, 170).fx( vfx.colorx, 1.0)
        clips = (clip1, clip2, clip3, clip4, clip5, clip6, clip7)
        
        
    final_clip_without_music = concatenate_videoclips(clips, method="compose")
    final_clip_without_music.write_videofile("final_video_without_music.mp4")
        

    


if __name__ == "__main__":
    download_youtube_videos()
    edit_videos()

