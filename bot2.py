#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, subprocess
import asyncio
from ffmpeg import FFmpeg
from moviepy.editor import *
import glob

path = '/usr/local/bin/chromedriver'
service = Service(path)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#driver = webdriver.Chrome(service=service, options=chrome_options)
#driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
#creating a webdriver object and opening the webpage 
driver = webdriver.Chrome() 
# Go to the page with the videos 
driver.get("https://proxitok.pabloferreiro.es/tag/gamer") 
 
# Get all video elements from the page 
videos = driver.find_elements_by_css_selector('video') 
 
# Download each video one by one 
for i, video in enumerate(videos[:10]): 

    # Get the source of the video element  
    src = video.get_attribute('src')  

    # Download the video  
    os.system(f"curl -o {i}.mp4 {src}")  

    print(f"Downloaded {i}.mp4")  

     # Close the browser window  
driver.quit()  

 # Concatenate all downloaded videos into one and rename it to final.mp4  

 clips = [VideoFileClip(file) for file in glob.glob("*.mp4")]  

 final_clip = concatenate_videoclips(clips)  

 final_clip.write_videofile("final.mp4")

 # Log into YouTube using Selenium and upload the concatenated file renamed to final mp4    
driver.get("https://accounts.google.com/ServiceLogin?service=youtube")
 
# Enter username and password and submit form
username = driver.find_element_by_id("Email")
password = driver.find_element_by_id("Passwd")
username.send_keys("samardehmohamad@gmail.com") # Replace with your username 
password.send_keys("M\G4iTlw$5$sAL.Ch^2s") # Replace with your password 
password.submit()  # Submit form to log in to YouTube account 
 
# Navigate to upload page and upload video file 
driver.get("https://www.youtube.com/upload")   # Go to upload page on YouTube 
uploadButton = driver.find_element_by_id('upload-prompt-box')   # Find the upload button on the page  
uploadButton.send_keys('./final.mp4')   # Replace with path and name of concatenated video file renamed to finalVideoFileName  
driver.close()
