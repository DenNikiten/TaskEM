from selenium.webdriver.common.by import By
import allure
from base.base_page import BasePage
from utilities.logger import Logger


class ShoppingCartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_btn = (By.CSS_SELECTOR, 'button[id="checkout"]')
        self.customer_info_page_url_text = "checkout-step-one.html"

    # Getters

    def get_checkout_btn(self):
        return self.element_is_clickable(self.checkout_btn)

    # Action

    def click_checkout_btn(self):
        self.get_checkout_btn().click()
        print("Click checkout button")

    # Method

    def product_confirmation(self):
        with allure.step('Product confirmation'):
            Logger.add_start_step(method='product_confirmation')
            self.click_checkout_btn()
            assert self.text_contains_in_url(self.customer_info_page_url_text), f"The text " \
                                                                                f"{self.customer_info_page_url_text} " \
                                                                                f"is not contained in url"
            Logger.add_end_step(url=self.driver.current_url, method='product_confirmation')