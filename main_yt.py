#!/usr/bin/env python3

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r'C:\\Users\\ToyinOlape\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)
driver.get("https://www.youtube.com/results?search_query=mobile+interface")

user_data1 = driver.find_elements_by_xpath('//*[@id="video-title"]')
links1 = []
for i in user_data1:
    links1.append(i.get_attribute('href'))
print(len(links1))

df1 = pd.DataFrame(columns = ['link', 'title', 'description','number of views', 'author', 'category'])

wait = WebDriverWait(driver, 10)
v_category = "mobile interface"
for x in links1:
    #Extract dates from for each user on a page
    driver.get(x)
    v_id = x
    v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.title yt-formatted-string"))).text
    v_description = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div#description yt-formatted-string"))).text
    v_no_views = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.view-count.style-scope"))).text
    v_author= wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a.yt-simple-endpoint.yt-formatted-string"))).text

    
    df1.loc[len(df1)] = [v_id,v_title, v_description, v_no_views, v_author,v_category]

df1.to_csv("../yt_data/yt1.csv")
print(len(links1))
print(df1.head())
