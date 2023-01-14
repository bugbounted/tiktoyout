 #!/usr/bin/env python3

import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Set up Chrome options for headless mode and disable GPU 
chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  

 # Create a new instance of the Chrome driver 
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options) 

 # Scrape 10 videos from TikTok every hour 
while True: 

    # Scrape 10 videos from TikTok 
    driver.get('https://www.tiktok.com/') 

    # Concatenate all videos into one file and rename it to final.mp4 
    os.system('ffmpeg -f concat -safe 0 -i mylist.txt -c copy final.mp4')

    # Auto upload the concatenated file to your YouTube channel using headless Selenium 
    driver.get('https://www.youtube.com/upload')

    # Upload the video to YouTube using Selenium 
    uploadButton = driver.find_element_by_id('upload-prompt-box')  
    uploadButton.send_keys(os.path.abspath('final'))  

    timeButton = driver .find_element_by_id('next-button')  
    timeButton .click()  

    titleField = driver .find_element_by_id('text-input')  
    titleField .send _keys ('My TikTok Video Compilation')  

     # Wait an hour before scraping again 
     time .sleep (3600)
