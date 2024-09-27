from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver.get("https://ya.ru/") #открывается первая страница
driver.get("https://vk.com/") #открывается вторая страница
sleep(50)