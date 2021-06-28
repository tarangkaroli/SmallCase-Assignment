import time

import allure
from selenium.webdriver import ActionChains

from locators.elementsAmazon import SetHomePageElements, ProductSearchListElements, ItemFormElements, CartPageElements


class SelectProductAmazon:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Select the First Item")
    def select_product_first(self):
        time.sleep(0.9)
        self.driver.find_element(*ProductSearchListElements.firstProductFromList).click()
        print("Selected first product")

    @allure.step("Get the price of the product")
    def get_price(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        price_product = self.driver.find_element(*ItemFormElements.priceOfProduct)
        return price_product.text

    @allure.step("Add the product to the cart")
    def add_to_cart(self):
        self.driver.find_element(*ItemFormElements.addToCartButton).click()
        time.sleep(3)
        self.driver.find_element(*ItemFormElements.closeSideCartPage).click()
        self.driver.find_element(*SetHomePageElements.cartLink).click()

    @allure.step("Get the updated quantity")
    def get_quantity_in_cart(self):
        quanta = self.driver.find_element(*CartPageElements.itemQuantityText)
        return quanta.get_attribute('value')

    @allure.step("Get price from the cart")
    def get_price_from_cart(self):
        price_in_cart = self.driver.find_element(*CartPageElements.totalAmount)
        return price_in_cart.text

    @allure.step("Remove the product from cart")
    def remove_from_cart(self):
        self.driver.find_element(*CartPageElements.removeProduct).click()

