#!/usr/bin/env python3

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service, options=chrome_options)
#driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)
url = "https://www.tiktok.com/"  # Replace with the URL you want to scrape from 
driver.get(url)


# Wait for the page to load and find all video elements on the page 
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for the elements to become available 
videos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".video-feed-item")))[:10]  # Get only 10 videos


# Download each video and save it in a folder called "videos" 
if not os.path.exists("videos"): os.mkdir("videos")   # Create a folder called "videos" if it doesn't exist yet 
for i, video in enumerate(videos):   # Loop through all videos on the page 

    # Get the download link of each video and download it using wget command line tool  
    download_link = video.find_element_by_css_selector("a").get_attribute("href")   # Get the download link of each video  

    subprocess.run(["wget", "-O", f"videos/video{i}.mp4", download_link])   # Download each video using wget command line tool and save it in "videos" folder with name "video{i}.mp4"

    
# Concatenate all downloaded videos into one file called final.mp4 using ffmpeg command line tool  
subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "listfile", "-c", "copy", "final.mp4"])   # Concatenate all downloaded videos into one file called final

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
