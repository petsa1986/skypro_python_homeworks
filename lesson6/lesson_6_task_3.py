from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 40, 0.1)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
wait.until (EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))
get_attribute = driver.find_element (By.ID,'award').get_attribute('src')
print(get_attribute)

driver.quit()