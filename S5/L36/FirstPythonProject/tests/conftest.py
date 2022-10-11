import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()
