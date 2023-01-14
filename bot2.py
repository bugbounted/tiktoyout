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
driver.get("https://proxitok.pabloferreiro.es/tag/gamer") 
  
#finding all the video elements on the page 
videos = driver.find_elements_by_xpath("//video[@class='video-js vjs-default-skin']") 
  
#creating a list to store all the video files 
video_files = [] 
  
#downloading 10 videos from the page without watermark 
for i in range(10): 

    #getting the source of each video element and downloading it to local directory 
    src = videos[i].get_attribute('src') 

    #generating a unique name for each video file using its index in list of videos  
    filename = "video" + str(i) + ".mp4"

    #downloading each video file to local directory with unique name generated above  														     
    os.system("wget -O " + filename + " " + src)

    #appending each downloaded video file to list of video files  
    video_files.append(filename) 

   #closing the web browser window after downloading all 10 videos     driver.close()

   #creating an instance of concatenate class from moviepy library and passing list of downloaded videos as argument     
   final_clip = concatenate_videoclips(video_files)

   #writing the concatenated clip to local directory with name final.mp4     
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
