from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))


def test_form_elements():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(4)
    driver.maximize_window()

    driver.find_element(By.CSS_SELECTOR, 'input[name = "first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "address"]').send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "zip-code"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[name = "city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name = "company"]').send_keys("SkyPro")

    button = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    ActionChains(driver).move_to_element(button).perform()
    button.click()

    zip_code_color = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
    assert zip_code_color == 'rgba(248, 215, 218, 1)'

    other_fields = ["#first-name", "#last-name", "#address", "#e-mail",
                    "#phone", "#city", "#country", "#job-position", "#company"]
    for field in other_fields:
        field_color = driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color")
    assert field_color == 'rgba(209, 231, 221, 1)'

    driver.quit()