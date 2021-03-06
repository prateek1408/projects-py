# importing webdriver which is neccessary to load the browser
from selenium import webdriver
import time

url="https://www.youtube.com"
searchstring="music"
WAIT=3      #depends upon your internet speed
driver=webdriver.Chrome() 
driver.get(url)  

time.sleep(WAIT)
search_box=driver.find_element_by_xpath('//*[@id="search"]')
search_box.send_keys(searchstring)

search_btn=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
search_btn.click()

time.sleep(WAIT)
video=driver.find_element_by_xpath('//*[@id="title-wrapper"]/h3')
video.click()
