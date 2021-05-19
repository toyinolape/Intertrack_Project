from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

keywords_designr = ["product design","ux research","userinterface-design","figma","user-experience-design"]

#keywords = ["product design","ux research","user interface design","figma","user experience design"]  
keywords = keywords_designr[0]

def search(keywords):
    print(keywords)
    keyword = keywords.split(" ")
    keyword = keyword[0]+''.join(['%20'+k for k in keyword[1:]])
    #keywords = keywords[0]+'+'+keywords[1] if len(keywords) < 1 else keywords[0]
    return 'https://medium.com/search?q=' + keyword  
url = search(keywords)


path = r'C:\\Users\\ToyinOlape\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = path)


driver.get(url)

#Title
title = []
titles = driver.find_elements_by_xpath("//div[@class='section-content']/div/h3")
for a in titles:
    title.append(a.text)

#Upvotes
upvote = []
upvotes =driver.find_elements_by_xpath("//div[@class='multirecommend js-actionMultirecommend u-flexCenter']/span/button")
for b in upvotes:
    upvote.append(b.text)
#Links
link = []
links = driver.find_elements_by_xpath("//div[@class='postArticle-content']/a")
for c in links:
    link.append(c.get_property('href'))

#image link 
img_url = []
img_urls = driver.find_elements_by_xpath("//div[@class='progressiveMedia js-progressiveMedia graf-image is-canvasLoaded is-imageLoaded']/img")
for d in img_urls:
    img_url.append(d.get_property('src'))

author = []
authors = driver.find_elements_by_xpath("//div[@class='postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis']/a")
for e in authors:
    author.append(e.text)


tot = {"Title":[], "Link":[], "Price":[], "Resource_Type":[], "Upvotes":[], "Keyword":[],"Source":[], "Source_url":[], "Thumbnail":[]}

try:
    for i in range(len(links)):
        tot["Title"].append(title[i])
        tot["Link"].append(link[i])
        tot["Price"].append("Free")
        tot["Resource_Type"].append("article")
        tot["Upvotes"].append(upvote[i])
        tot["Keyword"].append(keywords)
        tot["Source"].append("medium")
        tot["Source_url"].append(author[i])
        #tot["Thumbnail"].append(img_url[i])
        df5 = pd.DataFrame(tot,columns=["Title", "Link", "Price", "Resource_Type", "Upvotes", "Keyword","Source", "Source_url"])  

finally:
    driver.quit()      

#df1.shape, df2.shape,df3.shape,df4.shape,df5.shape
#md = df1.append(df2.append(df3.append(df4.append(df5))))

md.to_csv("md.csv")