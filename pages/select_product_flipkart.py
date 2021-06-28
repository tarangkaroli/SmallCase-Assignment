import allure
import time
from locators.elementsFlipkart import ItemSearchListElements, ItemFormElements, CartPageElements


class SelectProduct:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Select the First Item")
    def select_product_first(self):
        self.driver.find_element(*ItemSearchListElements.firstElementFromList).click()

    @allure.step("Get the price of the product")
    def get_price(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        price_product = self.driver.find_element(*ItemFormElements.priceOfProduct)
        return price_product.text

    @allure.step("Add the product to the cart")
    def add_to_cart(self):
        self.driver.find_element(*ItemFormElements.addToCartButton).click()
        time.sleep(3)

    @allure.step("Change the quantity of the product")
    def change_quantity(self, way, quantity):
        if way == 'inc':
            for i in range(quantity):
                self.driver.find_element(*CartPageElements.increaseItemButton).click()
        elif way == 'dec':
            for i in range(quantity):
                self.driver.find_element(*CartPageElements.decreaseItemButton).click()
        time.sleep(3)

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
        self.driver.find_element(*CartPageElements.confirmRemove).click()
