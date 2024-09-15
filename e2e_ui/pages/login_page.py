from selenium.webdriver.common.by import By
from utilities.logger import Logger
from base.base_page import BasePage
import allure


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_page_url = "https://www.saucedemo.com/"
        self.username = "standard_user"
        self.password = "secret_sauce"
        self.username_locator = (By.CSS_SELECTOR, 'input[id="user-name"]')
        self.password_locator = (By.CSS_SELECTOR, 'input[id="password"]')
        self.login_button = (By.CSS_SELECTOR, 'input[id="login-button"]')
        self.product_page_title_text_locator = (By.CSS_SELECTOR, 'span[class="title"]')
        self.product_page_title_text = "Products"
        self.product_page_url_text = "inventory.html"

    # Getters

    def get_username(self):
        return self.element_is_visible(self.username_locator)

    def get_password(self):
        return self.element_is_visible(self.password_locator)

    def get_login_button(self):
        return self.element_is_visible(self.login_button)

    def get_title_text_product_page(self):
        return self.element_is_present(self.product_page_title_text_locator)

    # Actions

    def input_username(self, username):
        self.get_username().send_keys(username)
        print("Input user name")

    def input_password(self, pwd):
        self.get_password().send_keys(pwd)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Method

    def authorisation(self):
        with allure.step("Authorisation"):
            Logger.add_start_step(method='authorisation')
            self.open(self.login_page_url)
            self.input_username(self.username)
            self.input_password(self.password)
            self.click_login_button()
            assert self.text_contains_in_url(self.product_page_url_text), f"The text {self.product_page_url_text} " \
                                                                          f"is not contained in url"
            self.assert_word(self.get_title_text_product_page(), self.product_page_title_text), "The text " \
                                                                                                "does not match"
            Logger.add_end_step(url=self.driver.current_url, method='authorisation')
