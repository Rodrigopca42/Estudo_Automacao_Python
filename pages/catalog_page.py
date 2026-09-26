from selenium.webdriver.common.by import By


class CatalogPage:

    # ========================================================
    # LOCATORS
    # ========================================================

    BLACK_HEELS = (By.ID, "product-1")
    BRONZE_SANDALS = (By.ID, "product-2")
    BROWN_SHADES = (By.ID, "product-3")
    GREY_JACKET = (By.ID, "product-4")
    NOIR_JACKET = (By.ID, "product-5")
    STRIPED_TOP = (By.ID, "product-6")
    WHITE_SANDALS = (By.ID, "product-7")
    
    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(self, driver):
        self.driver = driver

    # ========================================================
    # AÇÕES
    # ========================================================

    def acessar_black_heels(self):
        black_heels = self.driver.find_element(
            *self.BLACK_HEELS
        )

        black_heels.click()

    def acessar_bronze_sandals(self):
        bronze_sandals = self.driver.find_element(
            *self.BRONZE_SANDALS
        )

        bronze_sandals.click()

    def acessar_brown_shades(self):
        brown_shades = self.driver.find_element(
            *self.BROWN_SHADES
        )

        brown_shades.click()

    def acessar_grey_jacket(self):
        grey_jacket = self.driver.find_element(
            *self.GREY_JACKET
        )

        grey_jacket.click()

    def acessar_noir_jacket(self):
        noir_jacket = self.driver.find_element(
            *self.NOIR_JACKET
        )

        noir_jacket.click()

    def acessar_striped_top(self):
        striped_top = self.driver.find_element(
            *self.STRIPED_TOP
        )

        striped_top.click()

    def acessar_white_sandals(self):
        white_sandals = self.driver.find_element(
            *self.WHITE_SANDALS
        )

        white_sandals.click()







