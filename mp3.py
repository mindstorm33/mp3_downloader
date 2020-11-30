#!python3

import sys,time
from selenium import webdriver 

browser = webdriver.Chrome()
search = ' '.join(sys.argv[1:])

browser.get('https://youtube.com')
search_box = browser.find_element_by_tag_name('input')
search_box.send_keys(search)
search_box.submit()

time.sleep(3)
vid_link = browser.find_element_by_id('video-title').get_attribute('href')

browser.get('https://y2mate.com')
search_box = browser.find_element_by_tag_name('input')
search_box.send_keys(vid_link)
search_box.submit()

time.sleep(3)
browser.find_element_by_link_text('mp3').click()
time.sleep(3)
browser.find_element_by_link_text('Download').click()
time.sleep(3)
try:
    browser.find_element_by_link_text('Download .mp3').click()
except:
    time.sleep(5)
    browser.find_element_by_link_text('Download .mp3').click()
    








