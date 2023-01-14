import requests
from bs4 import BeautifulSoup
import os
import shutil
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options 


#Scraping 10 videos from TikTok using requests and BeautifulSoup library 
url = 'https://www.tiktok.com/' 
page = requests.get(url) 
soup = BeautifulSoup(page.content, 'html5lib') 
videos = soup.find_all('video', class_='jsx-3523532890 video-player') 

 #Downloading the videos from TikTok using shutil library  
for i in range(10):  
    video_url = videos[i]['src']  

    # Download the video  
    r = requests.get(video_url, stream=True)  

    # Download started  
    with open('video'+str(i)+'.mp4', 'wb') as f:  

        shutil.copyfileobj(r.raw, f)  

    # Download completed  

    print('Downloaded ' + str(i+1) + ' video!')  

     #Concatenating all the downloaded videos into one file using os library    
os.system("ffmpeg -f concat -safe 0 -i mylist.txt -c copy final_video.mp4") 

 #Renaming the concatenated file to final.mp4 using os library    
os.rename("final_video.mp4", "final.mp4") 

 #Auto Uploading the concatenated file to YouTube Channel using headless selenium    
options=Options() 										#creating options for headless browser session 								#adding arguments for headless browser session  
options.add_argument("--headless") 
options.add_argument("--disable-gpu") 
driver=webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver",chrome_options=options) 
driver.get("https://www .youtube .com/upload") 
driver.find_element_by_id ("text").send_keys("final .mp4") 
driver.find_element _by _id("upload-prompt-box").click()
