import allure
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utilities.logger import Logger


class FinalPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.successes_word_loc = (By.CSS_SELECTOR, 'h2[class="complete-header"] ')
        self.successes_text = "Thank you for your order!"
    # Getters

    def get_successes_word(self):
        return self.element_is_present(self.successes_word_loc)

    # Actions

    # Method

    def complete_order(self):
        with allure.step('Complete order!'):
            Logger.add_start_step(method='complete_order')
            self.assert_word(self.get_successes_word(), self.successes_text)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='complete_order')