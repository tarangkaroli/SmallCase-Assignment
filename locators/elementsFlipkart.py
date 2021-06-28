from selenium.webdriver.common.by import By


class SetHomePageElements:
    search_TextBox = (By.XPATH, "//input[@type='text' and contains(@title, 'Search for')]")
    searchIcon = (By.XPATH, "//button[@type='submit']")
    cartLink = (By.XPATH, "//a[contains(@href, 'viewcart')]")
    loginLink = (By.XPATH, "//a[contains(@href, 'login')]")
    closeLoginWindow = (By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")


class ItemSearchListElements:
    listItems = (By.XPATH, "//*[contains(@class, '_3Mn1Gg')][2]//div[contains(@class, '_1AtVbE col-12-12')]")
    firstElementFromList = (By.XPATH, "//*[contains(@class, '_3Mn1Gg')][2]//div[contains(@class, '_1AtVbE col-12-12')][1]")


class ItemFormElements:
    priceOfProduct = (By.CSS_SELECTOR, "._30jeq3._16Jk6d")
    # addToCartButton = (By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")
    addToCartButton = (By.XPATH, "//button[text()='ADD TO CART']")


class CartPageElements:
    increaseItemButton = (By.XPATH, "//button[@class='_23FHuj' and text()='+']")
    decreaseItemButton = (By.XPATH, "//button[@class='_23FHuj' and text()='-']")
    itemQuantityText = (By.XPATH, "//input[@type='text' and @class='_253qQJ']")
    totalAmount = (By.XPATH, "//div[@class='Ob17DV _3X7Jj1']//span")
    removeProduct = (By.XPATH, "//*[text()='Remove']")
    confirmRemove = (By.XPATH, "//*[@class='_3dsJAO _24d-qY FhkMJZ' and text() = 'Remove']")
