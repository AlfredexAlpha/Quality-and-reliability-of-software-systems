from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, os
import json
import requests
from selenium.webdriver.common.keys import Keys

src_path = ""

def safariSetup():
    driver =  webdriver.Chrome(ChromeDriverManager().install())
    
    #accept cookies
    driver.get("https://soundcloud.com/")
    time.sleep(3)
    cookieBttn = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
    if cookieBttn != None: cookieBttn.click()

    main(driver)
                
def collectLinks(driver):
    #Collects the links from the site
    scroll_content = driver.find_element(By.CLASS_NAME, 'playableTile__descriptionContainer')
    scroll_elements = driver.find_elements(By.CLASS_NAME, 'badgeList__item')
    return [elem.find_element(By.CSS_SELECTOR, 'a.sc-link-primary').get_attribute('href') for elem in scroll_elements]

def downloadLinks(links, driver):
    global src_path
    linkCounter = 0
    dudLinks = {}
    for i in links:
        driver.get('https://sclouddownloader.net//')
        time.sleep(3)
        try:
            downloadBox = driver.find_element_by_xpath("//input[@name='sound-url']")
            downloadBox.send_keys(links[linkCounter] + '\n')
            time.sleep(4)
            downloadButton = driver.find_element_by_xpath("//*[contains(text(), 'Download Track ')]")
            time.sleep(6)
            downloadButton.click()
            time.sleep(6)
            for element in driver.find_elements_by_tag_name('i'):
                if (element.text != "Download Another Track" and element.text != '"Download"' and element.text != "SoundCloud Playlist Downloader"):
                    dudLinks[element.text] = links[linkCounter]
        except:
            print("Something went wrong\n")
        linkCounter = linkCounter + 1
    newFiles = Duds.getFiles(src_path)
    checkFiles = Duds.checkDict(dudLinks)
    new_list = Duds.notMatches(newFiles, checkFiles)
    Duds.printDuds(new_list)
        
               
def main(driver):
    driver.maximize_window()
    links = collectLinks(driver)
    downloadLinks(links, driver)
    driver.quit()
safariSetup()