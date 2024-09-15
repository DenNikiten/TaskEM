import random
import allure
from selenium.webdriver.common.by import By
from utilities.logger import Logger
from base.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.select_products = (By.CSS_SELECTOR, 'div[class="inventory_item_description"]')
        self.shopping_cart = (By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
        self.select_product_in_shopping_cart = (By.CSS_SELECTOR, 'div[class="cart_item"]')

    # Getters

    def get_select_products(self):
        return self.elements_are_present(self.select_products)

    def get_product_name_for_loc(self, product_name):
        return product_name.lower().replace(" ", "-")

    def get_shopping_cart(self):
        return self.element_is_clickable(self.shopping_cart)

    def get_one_of_the_products(self):
        item_list = self.get_select_products()
        item = item_list[random.randint(0, 5)]
        product_name, product_desc, product_price, _ = item.text.splitlines()
        return [product_name, product_desc, product_price]

    def get_product_in_shopping_cart(self):
        item = self.element_is_present(self.select_product_in_shopping_cart)
        _, product_name, product_desc, product_price, _ = item.text.splitlines()
        return [product_name, product_desc, product_price]

    # Actions

    def add_the_selected_product_to_the_cart(self, product_name_for_loc):
        self.element_is_clickable((By.CSS_SELECTOR, f'button[id="add-to-cart-{product_name_for_loc}"]')).click()
        print("Add the selected product to the cart")

    def click_shopping_cart(self):
        self.get_shopping_cart().click()
        print("Click shopping cart")

    # Method

    def select_product(self):
        with allure.step('Select product'):
            product_name, _, _ = self.get_one_of_the_products()
            product_name_for_loc = self.get_product_name_for_loc(product_name)
            self.add_the_selected_product_to_the_cart(product_name_for_loc)
            return product_name

    def select_product_and_go_to_the_shopping_cart_and_check_out_product(self):
        with allure.step('Select product and go to the shopping cart and check out product'):
            Logger.add_start_step(method='select_product_and_go_to_the_shopping_cart_and_check_out_product')
            product_name = self.select_product()
            self.click_shopping_cart()
            product_name_cart_page, _, _ = self.get_product_in_shopping_cart()
            assert product_name == product_name_cart_page, "The product does not match the one in the shopping cart"
            Logger.add_end_step(url=self.driver.current_url, method='select_product_and_go_to_the_shopping_'
                                                                    'cart_and_check_out_product')
