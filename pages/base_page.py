class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_home_page_flipkart(self, config):
        self.driver.get(config["tested_page_flipkart"])

    def open_home_page_amazon(self, config):
        self.driver.get(config["tested_page_amazon"])
