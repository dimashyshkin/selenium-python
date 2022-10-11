from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button_locator = (By.ID, "add_btn")
    __row_1_input_element = (By.XPATH, "//div[@id='row1']/input")
    __row_2_input_element = (By.XPATH, "//div[@id='row2']/input")
    __row_1_save_button = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row_2_save_button = (By.XPATH, "//div[@id='row2']/button[@name='Save']")
    __confirmation_element = (By.ID, "confirmation")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_second_row(self):
        super()._click(self.__add_button_locator)
        super()._wait_until_element_is_visible(self.__row_2_input_element)

    def is_row2_displayed(self) -> bool:
        return super()._is_displayed(self.__row_2_input_element)