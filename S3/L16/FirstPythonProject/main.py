# Open browser
# selenium 4
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
time.sleep(5)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5)
