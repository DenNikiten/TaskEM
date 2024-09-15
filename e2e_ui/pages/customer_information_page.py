from selenium.webdriver.common.by import By
import allure
from utilities.logger import Logger
from base.base_page import BasePage
from generator.generator import generated_person


class CustomerInformationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = (By.CSS_SELECTOR, 'input[id="first-name"]')
        self.last_name = (By.CSS_SELECTOR, 'input[id="last-name"]')
        self.postal_code = (By.CSS_SELECTOR, 'input[id="postal-code"]')
        self.continue_button = (By.CSS_SELECTOR, 'input[id="continue"]')
        self.payment_page_url_text = "checkout-step-two.html"

    # Getters

    def get_first_name(self):
        return self.element_is_visible(self.first_name)

    def get_last_name(self):
        return self.element_is_visible(self.last_name)

    def get_postal_code(self):
        return self.element_is_visible(self.postal_code)

    def get_continue_button(self):
        return self.element_is_visible(self.continue_button)

    # Actions

    def input_first_name(self, firstname):
        self.get_first_name().send_keys(firstname)
        print("Input first name")

    def input_last_name(self, lastname):
        self.get_last_name().send_keys(lastname)
        print("Input last name")

    def input_postal_code(self, postalcode):
        self.get_postal_code().send_keys(postalcode)
        print("Input postal code")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")

    def add_personal_info(self):
        person_info = next(generated_person())
        self.input_first_name(person_info.first_name)
        self.input_last_name(person_info.last_name)
        self.input_postal_code(person_info.postal_code)
        print("Add personal info")

    # Method

    def fill_customer_information(self):
        with allure.step('Fill customer information'):
            Logger.add_start_step(method='fill_customer_information')
            self.add_personal_info()
            self.click_continue_button()
            assert self.text_contains_in_url(self.payment_page_url_text), f"The text {self.payment_page_url_text} " \
                                                                          f"is not contained in url"
            Logger.add_end_step(url=self.driver.current_url, method='fill_customer_information')