from selenium.webdriver.common.by import By


class SetHomePageElements:
    search_TextBox = (By.ID, "twotabsearchtextbox")
    searchIcon = (By.ID, "nav-search-submit-button")
    cartLink = (By.ID, "nav-cart")
    loginLinkNav = (By.ID, "nav-link-accountList-nav-line-1")
    # loginLink = (By.XPATH, "//a[contains(@href, '/login')]")
    closeLoginWindow = (By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")


class ProductSearchListElements:
    listItems = (By.XPATH, "//*[contains(@class, '_3Mn1Gg')][2]//div[contains(@class, '_1AtVbE col-12-12')]")
    firstProductFromList = (By.XPATH, "//*[contains(@cel_widget_id, 'MAIN-SEARCH_RESULTS-2')]//*[contains(@class, 'a-section a-spacing-medium')][1]//div[contains(@class, 's-image-fixed-height')]//img")


class ItemFormElements:
    priceOfProduct = (By.ID, "priceblock_dealprice")
    addToCartButton = (By.ID, "add-to-cart-button")
    proceedToCheckOut = (By.ID, "a-button-input")
    closeSideCartPage = (By.ID, "attach-close_sideSheet-link")


class CartPageElements:
    # increaseItemButton = (By.XPATH, "//button[@class='_23FHuj' and text()='+']")
    # decreaseItemButton = (By.XPATH, "//button[@class='_23FHuj' and text()='-']")
    itemQuantityText = (By.CSS_SELECTOR, "#a-autoid-0-announce .a-dropdown-prompt")
    totalAmount = (By.ID, "sc-subtotal-amount-buybox")
    removeProduct = (By.XPATH, "//span[@data-action='delete']")
