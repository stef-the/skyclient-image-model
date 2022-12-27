from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

url = 'https://teachablemachine.withgoogle.com/train/image'

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(url)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'sample-input-list'))
    )
    print(element)
finally:
    driver.quit()