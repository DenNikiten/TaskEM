import allure
from pages.customer_information_page import CustomerInformationPage
from pages.final_page import FinalPage
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage


class TestBuyProduct:

    @allure.description("Test buy product")
    def test_buy_product(self, browser):
        login_page = LoginPage(browser)
        login_page.authorisation()

        product_page = ProductPage(browser)
        product_page.select_product_and_go_to_the_shopping_cart_and_check_out_product()

        shopping_cart_page = ShoppingCartPage(browser)
        shopping_cart_page.product_confirmation()

        customer_information_page = CustomerInformationPage(browser)
        customer_information_page.fill_customer_information()

        payment_page = PaymentPage(browser)
        payment_page.click_finish_button()

        final_page = FinalPage(browser)
        final_page.complete_order()



