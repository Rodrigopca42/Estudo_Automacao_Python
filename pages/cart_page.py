from selenium.webdriver.common.by import By


class CartPage:

    # ========================================================
    # PRODUTO 1
    # ========================================================

    CONTAINS_PRODUCT_1 = (By.XPATH, "//div/form/div[1]")
    IMAGE_PRODUCT_1 = (By.XPATH, "//div[1]/div[1]/img")
    TITLE_PRODUCT_1 = (By.XPATH, "//div[1]/div/h3/a")
    DESCRIPTION_PRODUCT_1 = (By.XPATH, "//div[1]/div[1]/div/p[1]")
    UNIT_PRICE_PRODUCT_1 = (By.XPATH, '//*[@id="drawer"]/div/form/div[1]/div[2]')
    QUANTITY_PRODUCT_1 = (By.XPATH, "//div[1]/div[3]/input")
    TOTAL_PRICE_PRODUCT_1 = (By.XPATH, "//div[1]/div[4]")
    DELETE_PRODUCT_1 = (By.XPATH, "//div[1]/div[5]/a")

    # ========================================================
    # PRODUTO 2
    # ========================================================

    CONTAINS_PRODUCT_2 = (By.XPATH, "//div/form/div[2]")
    IMAGE_PRODUCT_2 = (By.XPATH, "//div[2]/div[1]/img")
    TITLE_PRODUCT_2 = (By.XPATH, "//div[2]/div[1]/div/h3/a")
    DESCRIPTION_PRODUCT_2 = (By.XPATH, "//div[2]/div[1]/div/p[1]")
    UNIT_PRICE_PRODUCT_2 = (By.XPATH, "//div[2]/div[2]")
    QUANTITY_PRODUCT_2 = (By.XPATH, "//div[2]/div[3]/input")
    TOTAL_PRICE_PRODUCT_2 = (By.XPATH, "//div[2]/div[4]")
    DELETE_PRODUCT_2 = (By.XPATH, "//div[2]/div[5]/a")

    # ========================================================
    # PRODUTO 3
    # ========================================================

    CONTAINS_PRODUCT_3 = (By.XPATH, "//div/form/div[3]")
    IMAGE_PRODUCT_3 = (By.XPATH, "//div[3]/div[1]/img")
    TITLE_PRODUCT_3 = (By.XPATH, "//div[3]/div[1]/div/h3/a")
    DESCRIPTION_PRODUCT_3 = (By.XPATH, "//div[3]/div[1]/div/p[1]")
    UNIT_PRICE_PRODUCT_3 = (By.XPATH, "//div[3]/div[2]")
    QUANTITY_PRODUCT_3 = (By.XPATH, "//div[3]/div[3]/input")
    TOTAL_PRICE_PRODUCT_3 = (By.XPATH, "//div[3]/div[4]")
    DELETE_PRODUCT_3 = (By.XPATH, "//div[3]/div[5]/a")

    # ========================================================
    # CHECKOUT
    # ========================================================

    CHECK_OUT = (By.XPATH, "//div[4]/input")

    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(self, driver):
        self.driver = driver

    # ========================================================
    # HELPERS
    # ========================================================

    def localizar_produto(self, locator):
        return self.driver.find_element(*locator)

    def destacar_produto(self, locator):
        elemento = self.localizar_produto(locator)

        self.driver.execute_script(
            """
            arguments[0].style.border = '3px solid green';
            arguments[0].style.boxSizing = 'border-box';
            """,
            elemento
        )

    def produto_1_adicionado(self):
        return self.localizar_produto(
            self.CONTAINS_PRODUCT_1
        )

    def produto_2_adicionado(self):
        return self.localizar_produto(
            self.CONTAINS_PRODUCT_2
        )

    def produto_3_adicionado(self):
        return self.localizar_produto(
            self.CONTAINS_PRODUCT_3
        )

    def destacar_produto_1(self):
        self.destacar_produto(
            self.CONTAINS_PRODUCT_1
        )

    def destacar_produto_2(self):
        self.destacar_produto(
            self.CONTAINS_PRODUCT_2
        )

    def destacar_produto_3(self):
        self.destacar_produto(
            self.CONTAINS_PRODUCT_3
        )

    def acessar_checkout(self):
        checkout = self.localizar_produto(
            self.CHECK_OUT
        )

        checkout.click()