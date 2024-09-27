from time import sleep

driver = webdriver.Chrome()
driver.get ("http://uitestingplayground.com/classattr")

for i in range(3):
    blue_button=driver.find_element (
        "xpath","//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
    sleep(2)
    driver.switch_to.alert.accept()

