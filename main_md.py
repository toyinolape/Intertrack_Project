#!/usr/bin/env python3

from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search(keywords):
    keywords = keywords.split(" ")
    return 'https://medium.com/search'+'?q=' +keywords[0]+'%20'+keywords[1]

url = search("web design")

path = r'C:\\Users\\ToyinOlape\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)
driver.get(url)

titles =driver.find_elements_by_xpath("//div[@class='section-content']/div/h3")
for title in titles:
    print(title.text)