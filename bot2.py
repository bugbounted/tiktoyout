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
browser.get('https://proxitok.pabloferreiro.es/tag/gamer') 
wait = WebDriverWait(browser, 10) 
  
#finding all the video links on the page using XPATH selector 
video_links = browser.find_elements_by_xpath("//a[@class='video-link']") 

 #downloading 10 videos from the page  
for i in range(10): 

    #clicking on each video link to open it in a new tab  
    video_links[i].click() 

    #switching to the new tab  
    browser.switch_to_window(browser.window_handles[1]) 

    #waiting for the download button to appear  
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='download-button']"))) 

    #finding and clicking on the download button  
    downloadButton = browser.find_element_by_xpath("//button[@class='download-button']") 

    downloadButton .click() 

    #switching back to the main tab  
    browser.switch_to_window(browser.window_handles[0]) 

     #closing the current tab  
    browser.close() 

     #switching back to main tab again  
    browser.switch_to().window(browser.window_handles[0])     

     #moving all downloaded videos into one folder named 'videos'  																	                                                                                            
     os.mkdir('videos')      
     shutil.move('Downloads', 'videos')      
     files = os.listdir('videos/Downloads')      
     print(files)       #concatenating all downloaded videos into one file named 'final'      
     concatCommand = 'ffmpeg -f concat -safe 0 -i files -c copy final .mp4'      
     subprocess.call(concatCommand, shell=True)

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
