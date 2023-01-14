 #!/usr/bin/env python

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set environment variables for Gmail credentials 
GMAIL_USERNAME = os.environ['GMAIL_USERNAME'] 
GMAIL_PASSWORD = os.environ['GMAIL_PASSWORD'] 

 # Set headless Chrome options 
chrome_options = Options() 
chrome_options.add_argument("--headless") 

 # Create a new instance of the Chrome driver 
browser = webdriver.Chrome(options=chrome_options)

 # Go to the TikTok website and scrape 10 videos 
browser.get('https://www.tiktok.com/') 

 # Wait for the page to load before scraping the videos 
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'video-card__thumbnail'))) 

 # Scrape 10 videos from TikTok and save them to disk  
videos = browser.find_elements(By .CLASS _NAME, 'video-card__thumbnail')[:10]  

for i, video in enumerate(videos):  

    video .click()  

    WebDriverWait(browser, 10).until(EC .presence _of _element _located((By .CLASS _NAME, 'video-player__video')))  

    video _source = browser .find _element (By .CLASS _NAME, 'video-player__video') .get _attribute ('src')  

    with open('video_{}.mp4'.format (i), 'wb') as f:  

        f .write (requests .get (video _source) .content)  

        print ('Downloaded video {}'.format (i))  

        time .sleep (2)  

        browser .back ()  

        time .sleep (2)  

 # Concatenate all downloaded videos into one file named final mp4 using ffmpeg command line tool    
os .system ('ffmpeg -f concat -safe 0 -i <(for f in ./videos/*; do echo "file '$f'"; done) -c copy final.mp4')    

 # Log into YouTube using Selenium and upload the concatenated file renamed to final mp4    
browser.get("https://accounts.google.com/ServiceLogin?service=youtube")
 
# Enter username and password and submit form
username = browser.find_element_by_id("Email")
password = browser.find_element_by_id("Passwd")
username.send_keys("yourUsername") # Replace with your username 
password.send_keys("yourPassword") # Replace with your password 
password.submit()  # Submit form to log in to YouTube account 
 
# Navigate to upload page and upload video file 
browser.get("https://www.youtube.com/upload")   # Go to upload page on YouTube 
uploadButton = browser.find_element_by_id('upload-prompt-box')   # Find the upload button on the page  
uploadButton.send_keys('./final.mp4')   # Replace with path and name of concatenated video file renamed to finalVideoFileName  
