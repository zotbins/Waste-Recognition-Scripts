# Download Images

import os
import urllib.request as ulib
from bs4 import BeautifulSoup as BS
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver import Firefox

base_url = "https://www.google.com/search?q="

headers = {'User-Agent':'Chrome/41.0.2228.0'}

def get_links(search_term):
    links = set()
    search_term = search_term.replace(' ','+')
    url = base_url + search_term + '&client=firefox-b-1-d&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj5r9PdotPjAhVmFTQIHfG4C8QQ_AUIEigC&biw=798&bih=1079'

## Method 1
    driver = webdriver.Firefox()
    driver.get(url)
    
##    try:
##        driver.execute_script("window.scrollByPages(4)")
##        time.sleep(2)
##        driver.execute_script("window.scrollByPages(4)")
##        time.sleep(2)
##        driver.execute_script("window.scrollByPages(4)")
##        time.sleep(2)
##        driver.execute_script("window.scrollByPages(4)")
##        time.sleep(2)
##        driver.execute_script("window.scrollByPages(4)")
##        time.sleep(2)
##        driver.execute_script("window.scrollByPages(4)")
##        time.sleep(2)
##        driver.execute_script("window.scrollByPages(4)")
##        time.sleep(2)
##        driver.execute_script("window.scrollByPages(4)")
##        time.sleep(2)
##        driver.execute_script("window.scrollByPages(4)")
##    except:
##        print("ERROR")
##        driver.quit()

##    data = driver.page_source
    images = driver.find_elements_by_tag_name("img")
    for image in images:
##        print(image.get_attribute("class"))
        if image.get_attribute("class") == "rg_i Q4LuWd tx8vtf":
            image.click()
            time.sleep(0.2)
            data = driver.find_elements_by_class_name("n3VNCb")
            for img in data:
                link = img.get_attribute("src")
                if link.startswith("http") and "encrypted" not in link:
                    links.add(link)
            for img in data:
                link = img.get_attribute("src")
                if link.startswith("http") and "encrypted" not in link:
                    links.add(link)
##            data = driver.find_elements_by_tag_name("img")
####            print(len(data))
##            for img in data:
##                if img.get_attribute("class") == "n3VNCb":
####                    print("FOUND")
##                    link = img.get_attribute("src")
##                    if link.startswith("http"):
##                        links.add(link)
    
    driver.close()

#### Method 2
####    data = requests.get(url).text
##

## Convert source code to BS
##    soup = BS(data,"lxml")


#### Download full size images
##    links = [json.loads(i.text)["ou"] for i in soup.find_all("div",{"class":"rg_meta"})]

        
## Download small images
##    images = soup.find_all("img",{"src":True})
##    links = [image["src"] for image in images]
    
##    links = extract_links(data)
    return list(links)

def extract_links(data):
    links = []
    link = ""
    for i in data:
        link += i
        if i == '"':
            link = link.replace('"','')
            if link.startswith("http") and (link.endswith("jpg") or link.endswith("png")):
                links.append(link)
            link = ""
    return links

def save_images(links, search_term):
    directory = search_term.replace(' ','_')
    if not os.path.isdir(directory):
        os.mkdir(directory)
    for i, link in enumerate(links):
        try:
            save_path = os.path.join(directory,'{}_{:05}.jpg'.format(directory,i))
            ulib.urlretrieve(link,save_path)
        except:
            print("Error in image #" + str(i))

def display_links(links):
    for i in range(10):
        print(links[i])

def main():
    search_term = input("Enter Search Term: ")
    links = get_links(search_term)
    print("Length of List:",len(links))
    if len(links) > 10:
        display_links(links)
    else:
        for i in links:
            print(i)
##    save_images(links, search_term)

main()
