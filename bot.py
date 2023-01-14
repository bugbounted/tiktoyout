#!/usr/bin/env python3
import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Set environment variables for Gmail credentials 
GMAIL_USERNAME = os.environ['GMAIL_USERNAME'] 
GMAIL_PASSWORD = os.environ['GMAIL_PASSWORD'] 


# Set up headless Chrome browser options 
options = Options() 
options.headless = True 


# Create a new instance of the Chrome driver 
browser = webdriver.Chrome(options=options)


while True:

    # Scrape 10 videos from TikTok and save them to the current directory 
    subprocess.run(["scrape-tiktok", "-n", "10"])

    # Concatenate all downloaded videos into one file named final.mp4  
    subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "list.txt", "-c", "copy", "final.mp4"])

    # Log in to YouTube using Selenium and upload the concatenated video  
    browser.get('https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en-GB&ec=65620')

    username_input = browser.find_element_by_name('identifier')  # Find username input field by name attribute  
    username_input.send_keys(GMAIL_USERNAME)                  # Enter Gmail username into input field  

    nextButton = browser.find_element_by_id('identifierNext')   # Find Next button by id attribute  												   # Click Next button to proceed to password page  

    nextButton.click()                                        # Click Next button to proceed to password page  

    time.sleep(5)                                             # Wait 5 seconds for page to load before entering password  

    passwordInput = browser.find_element_by_name('password') # Find password input field by name attribute  

    passwordInput.send_keys(GMAIL_PASSWORD)               # Enter Gmail password into input field  

    signInButton = browser.find_element_by_id('passwordNext')     # Find Sign In button by id attribute    					       # Click Sign In button to log in to YouTube account    

    signInButton.click()                                     # Click Sign In button to log in to YouTube account    

    time.sleep(5)                                           # Wait 5 seconds for page to load before uploading video    

    uploadButton = browser.find_element_by_xpath('//*[@id="upload-prompt-box"]/div[2]/div[1]/span[1]')      # Find Upload Video button by xpath expression    

    uploadButton.click()                                     # Click Upload Video button    

    time.sleep(5)                                           # Wait 5 seconds for page to load before selecting file    

    selectFileInput = browser.find_element_by_xpath('//*[@id="start-upload-button-single"]')      # Find Select File input field by xpath expression    

    selectFileInput.send_keys(os._getcwd () + '/final.mp4 ')      # Enter path of concatenated video file into input field    

        publishButton = browser.find_element_by_xpath('//*[@id="upload-item-0"]/div[4]/div[1]/div[1]/span[1]')      # Find Publish Video button by xpath expression    

        publishButton.click()                                   # Click Publish Video button
