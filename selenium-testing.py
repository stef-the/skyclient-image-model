from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

url = 'https://teachablemachine.withgoogle.com/train/image'

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(url)