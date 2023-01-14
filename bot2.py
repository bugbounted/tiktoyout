#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, subprocess, shutil
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
url = "https://proxitok.pabloferreiro.es/tag/gamer"  #url of the webpage to be opened 
driver.get(url)   #opening the webpage 
wait = WebDriverWait(driver, 10) #waiting for 10 seconds for page to load completely 

 #finding all video elements on the page using XPATH selector 
video_elements = driver.find_elements_by_xpath("/html/body/section[2]/div[1]/article/div/div[3]/div[2]/div[2]/div/a[2]")  

 #downloading all videos one by one and saving them in a folder named 'videos' in current directory  
for i, video in enumerate(video_elements):    #enumerate is used to get index of each element in list 

    video_src = video.get_attribute('href')   #getting source of each video element

    if not os.path.exists('videos'):    #creating a folder named 'videos' if it doesn't exist already 
        os.mkdir('videos')

    file_name = f"videos/video_{i}.mp4"   #naming each downloaded file as 'video_(index).mp4'

    command = f"wget -O {file_name} {video_src}"   #using wget command to download each video from its source url and save it with given name in 'videos' folder

    subprocess.call(command, shell=True)   #executing wget command using subprocess library 

     #concatenating all downloaded videos into one and renaming it to final.mp4 using ffmpeg command line tool 
concatenateCommand = "ffmpeg -f concat -safe 0 -i <(for f in ./videos/*; do echo \"file '$f'\"; done) -c copy final.mp4"   #ffmpeg command for concatenation of multiple videos into one single file 

subprocess.call(concatenateCommand, shell=True)   #executing ffmpeg command using subprocess library 

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
