from selenium.webdriver.common.by import By

class MiniCartPage:


    # ========================================================
    # LOCATORS
    # ========================================================   

    REMOVE = (By.XPATH, "//div[1]/div[5]/a")
    CHECK_OUT = (By.XPATH, "//div[2]/input")

    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(self, driver):
        self.driver = driver


    # ========================================================
    # AÇÕES
    # ========================================================

    def delete(self):
        delete = self.driver.find_element(
            *self.REMOVE
        )

        delete.click()

    def acessar_check_out(self):
        check_out = self.driver.find_element(
            *self.CHECK_OUT
        )

        check_out.click()