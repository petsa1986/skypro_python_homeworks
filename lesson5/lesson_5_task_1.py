from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
chrome.get ('http://the-internet.herokuapp.com/add_remove_elements/')
for i in range(5):
    add_Button = chrome.find_element (By.XPATH, ("//button[text()='Add Element']")).click() 
sleep(10)    
chrome_delete_buttons =chrome.find_elements("xpath",'//button[text()="Delete"]')
print( f"размер списка кнопок Delete: {len(chrome_delete_buttons)}")

sleep(11)