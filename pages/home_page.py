from selenium.webdriver.common.by import By

class HomePage:

    # ========================================================
    # LOCATORS
    # ========================================================

    GREY_JACKET = (By.ID, "product-1")
    NOIR_JACKET = (By.ID, "product-2")
    STRIPED_TOP = (By.ID, "product-3")

    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(self, driver):
        self.driver = driver

    # ========================================================
    # AÇÕES
    # ========================================================

    def acessar_grey_jacket(self):
        produto = self.driver.find_element(
            *self.GREY_JACKET
        )

        produto.click()

    def acessar_noir_jacket(self):
        produto = self.driver.find_element(
            *self.NOIR_JACKET
        )    

        produto.click()

    def acessar_stirped_top(self):
        produto = self.driver.find_element(
            *self.STRIPED_TOP
        )

        produto.click()