import time

import allure
import pytest
from selenium import webdriver

from pages.search_item_amazon import ItemSearchFormAmazon
from pages.search_item_flipkart import ItemSearchFormFlipkart
from pages.select_product_amazon import SelectProductAmazon
from pages.select_product_flipkart import SelectProduct


@pytest.fixture
@allure.title("Setting up the browser")
def browser():
    # defining implicit wait time
    wait_time = 30

    """Creating the webdriver element for 
    Chrome Browser, and setting up the
    chrome webdriver options to execute"""

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option('useAutomationException', False)
    # chrome_options.add_argument('headless')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome('../chromedriver.exe', options=chrome_options)
    driver.implicitly_wait(wait_time)
    yield driver
    driver.quit()


@allure.title("Test1: Getting the price from Flipkart")
def get_price_flipkart(browser):
    print("\nVerifying the price on Flipkart")

    home_page = ItemSearchFormFlipkart(browser)
    home_page.open_page()
    home_page.product_search("mi phone")
    assert home_page.list_product_count() > 1

    result_page = SelectProduct(browser)
    result_page.select_product_first()

    print("\nThe price of the product is {0}".format(result_page.get_price()))

    result_page.add_to_cart()
    result_page.change_quantity('inc', 1)
    time.sleep(3)
    # assert result_page.get_quantity_in_cart() == "2"

    print("\nThe price of the cart is {0}".format(result_page.get_price_from_cart()))
    result_page.remove_from_cart()
    time.sleep(3)


@allure.title("Test2: Comparing prices between Flipkart & Amazon")
def compare_price(browser):
    print("\nCompare the prices on the Amazon & Flipkart")

    home_flipkart = ItemSearchFormFlipkart(browser)
    home_page_amazon = ItemSearchFormAmazon(browser)
    home_flipkart.product_search("iphone 12 128gb black")

    page_flipkart_result = SelectProduct(browser)
    page_flipkart_result.select_product_first()

    print("\nThe price of the product on Flipkart is {0}".format(page_flipkart_result.get_price()))
    page_flipkart_result.add_to_cart()
    time.sleep(3)

    price_flipkart = page_flipkart_result.get_price_from_cart()
    print("\nThe price of the product in cart on Flipkart is {0}".format(price_flipkart))
    page_flipkart_result.remove_from_cart()
    time.sleep(3)

    """Getting the price from Amazon website
    so that later it can be compared to
    price from the Flipkart website"""
    home_page_amazon.open_page()
    home_page_amazon.product_search("iphone 12 128gb black")

    result_page_amazon = SelectProductAmazon(browser)
    result_page_amazon.select_product_first()

    print("\nThe price of the product on Amazon is {0}".format(result_page_amazon.get_price()))
    result_page_amazon.add_to_cart()
    time.sleep(3)

    price_amazon = result_page_amazon.get_price_from_cart()
    print("\nThe price of the product in the cart on Amazon is {0}".format(price_amazon))
    result_page_amazon.remove_from_cart()
    time.sleep(3)

    if price_amazon == price_flipkart:
        print("\nThe price on both the sites is same")
    elif price_amazon > price_flipkart:
        print("Its cheaper on Flipkart")
    else:
        print("Its cheaper on Amazon")


@allure.title("Tests are executed from here")
def test_price(browser):
    get_price_flipkart(browser)
    compare_price(browser)


