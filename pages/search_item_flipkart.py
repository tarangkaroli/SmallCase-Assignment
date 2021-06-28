import allure
from locators.elementsFlipkart import SetHomePageElements, ItemSearchListElements


class ItemSearchFormFlipkart:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening Flipkart website")
    def open_page(self):
        self.driver.get("https://www.flipkart.com/")
        self.driver.find_element(*SetHomePageElements.closeLoginWindow).click()

    @allure.step("Searching the Product")
    def product_search(self, product):
        # self.driver.find_element(*SetHomePageElements.search_TextBox).click()
        self.driver.find_element(*SetHomePageElements.search_TextBox).send_keys(product)
        self.driver.find_element(*SetHomePageElements.searchIcon).click()

    @allure.step("Listing the Product Count")
    def list_product_count(self):
        product_count = self.driver.find_elements(*ItemSearchListElements.listItems)
        return len(product_count)
