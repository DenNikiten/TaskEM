import allure
from selenium.webdriver.common.by import By
from utilities.logger import Logger
from base.base_page import BasePage


class PaymentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.finish_button = (By.XPATH, '//button[@id="finish"] ')
        self.final_page_url_text = "checkout-complete.html"
        self.title_item_final_page = (By.XPATH, '//span[@class="title"] ')
        self.final_page_title_text = 'Checkout: Complete!'

    # Getters

    def get_finish_button(self):
        return self.element_is_visible(self.finish_button)

    def get_final_word(self):
        return self.element_is_visible(self.title_item_final_page)

    # Actions

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click Finish button")

    # Method

    def payment(self):
        with allure.step("Payment"):
            Logger.add_start_step(method='payment')
            self.click_finish_button()
            assert self.text_contains_in_url(self.final_page_url_text), f"The text {self.final_page_url_text} " \
                                                                        f"is not contained in url"
            self.assert_word(self.get_final_word(), self.final_page_title_text), "The text does not match"
            Logger.add_end_step(url=self.driver.current_url, method='payment')