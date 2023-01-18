from tiktokapi import TikTokApi
import moviepy.editor as mp
from youtube_bot import youtube

# Create an instance of the TikTokApi class
api = TikTokApi()

# Get the top 10 trending videos from TikTok
trending_videos = api.trending(count=10)

# Download each video and save it to a file in the current directory 
for video in trending_videos: 
    video.download(f"{video.id}.mp4") 
    
# Concatenate all of the downloaded videos into one file named final.mp4 
clips = [mp.VideoFileClip(f"{video.id}.mp4") for video in trending_videos] 
final_clip = mp.concatenate_videoclips(clips) 
final_clip.write_videofile("final.mp4")

obj = youtube()
obj.upload_video(video=r'C:\myvideo.mp4',
                    title="Tutorial #shorts ",
                    related_hashtag_keyword="fyp",
                    profile="Default")
