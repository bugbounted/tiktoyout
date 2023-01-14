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
driver = webdriver.Chrome(options=options)


while True:

    # Scrape 10 videos from TikTok and save them to the current directory 
    subprocess.run(["scrape-tiktok", "-n", "10"])

    # Concatenate all downloaded videos into one file named final.mp4  
    subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "list.txt", "-c", "copy", "final.mp4"])

    # Log in to YouTube using Selenium and upload the concatenated video  
    driver.get('https://www.youtube.com/upload')

 #finding and entering username and password fields  
username_field = driver.find_element_by_id('identifierId')  #finding username field by id  
username_field.send_keys(username) #entering username in the field  

 #clicking on next button after entering username  
nextButton = driver.find_element_by_id('identifierNext')  #finding next button by id  
nextButton.click()   

 #entering password after clicking on next button   												   		   	   	   	   	       	    	    	    	    

passwordField = driver.find_element_by_name('password') #finding password field by name  

 #entering password in the field and clicking on next button after entering password     

passwordField.send_keys(password)     

 #clicking on next button after entering password     

nextButton2 = driver.find_element_by_id('passwordNext')     

nextButton2.click()     

 #uploading video file to youtube channel using headless selenium     

uploadButton = driver.find_element_by_xpath("//input[@type='file']")     

uploadButton .sendKeys("final.mp4")
