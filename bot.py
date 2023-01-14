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
os .system ('ffmpeg -f concat -safe 0 -i <(for f in ./videos/*; do echo "file '$f'"; done) -c copy final mp4')    

 # Log into YouTube using Selenium and upload the concatenated file renamed to final mp4    
browser .get ('https://accounts google com/signin/v2/identifier?service=youtube&uilel=0&passive=true&continue=https%3A%2F%2Fwww youtube com%2Fsignin%3Faction handle signin%26app%3Ddesktop%26hl en-GB%26next %3Dhttps 3A 2F 2Fwww youtube com 2F&hl en-GB&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin')    

username = browser find element By XPATH ("//input[@type='email']") username send keys GMAIL USERNAME     password = browser find element By XPATH ("//input[@type='password']") password send keys GMAIL PASSWORD     login button = browser find element By XPATH ("//div[@id='identifierNext']") login button click ()     time sleep 5     upload button = browser find element By XPATH ("//div[@id='upload-prompt-box']") upload button click ()     time sleep 5     select file button = browser find element By XPATH ("//input[@type='file']") select file button send keys os path join os get cwd (), "final mp4"
