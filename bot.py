#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, subprocess
import asyncio
from ffmpeg import FFmpeg


# Create a new instance of the Chrome driver 
driver = webdriver.Chrome() 
  
# Go to the TikTok website 
driver.get("https://www.tiktok.com/") 

 # Wait for the page to load 
wait = WebDriverWait(driver, 10) 

 # Find the search bar and enter a query 
search_bar = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))) 
search_bar.send_keys("funny") 

 # Click on the search button 
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))) 
search_button .click() 

 # Wait for the results to load 
wait = WebDriverWait(driver, 10)  

 # Get all video links from the page and store them in a list  
video_links = []  

 # Iterate over all videos on the page and get their links  
for i in range(1, 11):  

    video = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='video-feed-item'][{i}]//a[@class='jsx-3523532887 video-feed-item__wrapper']")))  

    video_links .append(video .get_attribute('href'))  

    print (f"Found link {i}: {video .get_attribute('href')}")  

 # Download all videos from the list of links using youtube-dl command line tool  

 for link in video_links:  

     print (f"Downloading video from {link}...")  

     subprocess .run([ "youtube-dl", "-o", "videos/%(title)s-%(id)s", link])  

     print ("Done!")  

     time .sleep (2) # Sleep for 2 seconds before downloading next video to avoid getting blocked by TikTok server   

 # Concatenate all downloaded videos into one file named final .mp4 using ffmpeg command line tool   

subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "mylist.txt", "-c", "copy", "final.mp4"])

 # Concatenate all downloaded videos into one file named final mp4 using ffmpeg command line tool    
os.system('ffmpeg -f concat -safe 0 -i <(for f in ./videos/*; do echo "file '$f'"; done) -c copy final.mp4')    

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
