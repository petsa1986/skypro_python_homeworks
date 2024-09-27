from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

count = 0
driver.get('http://uitestingplayground.com/dynamicid')
blue_button =  driver.find_element (
    "xpath", '//button [text()="Button with Dynamic ID"]').click()

for _ in range (3):
    blue_button =  driver.find_element(
        "xpath", '//button [text()="Button with Dynamic ID"]').click()
    count = count + 1
    sleep(2)
    print(count)