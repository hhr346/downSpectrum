"""
This is a crawling program to get the txt of all the orbits on the website 
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard
 
def getCode():
    browser = webdriver.Chrome()
    browser.get('https://data.cresda.cn/#/home')
    print('Get in the website!')
    time.sleep(1)
    print('Please login in manually')
    input()
    browser.get('https://data.cresda.cn/#/mapSearch')
    print('Now select the date you want')
    input()

    # Find the select button
    i = 0
    while(1):
        try: 
            box = browser.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[1]/div[4]/div[4]/div[2]/div[2]/div[2]/table/thead/tr/th[1]/div/label')
            next = browser.find_element(by=By.XPATH, value='//*[@id="app"]/div/div[1]/div[4]/div[4]/div[2]/div[3]/div[4]/span[3]/i')
            i += 1
            box.click()
            time.sleep(2)
            next.click()
            time.sleep(2)
            browser.implicitly_wait(20)
            if i%60 == 0:
                print('Please check whether it misses')
                a = input()
                # the limit is 300???
                if a == 'q':
                    break
        except Exception as error:
            print(error)
            i -= 1

    print('Download the metadata!')
    input()
    browser.close()
getCode()
 