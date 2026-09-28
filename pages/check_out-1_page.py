from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.configuracoes import TIMEOUT



class CheckOut1Page:

    # ========================================================
    # LOCATORS
    # ========================================================

    QUANTIDADE = (By.XPATH, "//div[2]/div[3]/input")
    DELETE = (By.XPATH, "//div[2]/div[5]/a")
    CONTINUE_SHOPPING = (By.XPATH, "//div[2]/div[1]/a")
    ADD_NOTE = (By.ID, "note")
    UPDATE = (By.XPATH, "//div[3]/div[2]/input[1]")
    CHECK_OUT = (By.XPATH, "//div[3]/div[2]/input[2]")

    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(self, driver):
        self.driver = driver


    # ========================================================
    # AÇÕES
    # ========================================================


    def alterar_quantidade(self, nova_quantidade):
        quantidade = self.driver.find_element(
        *self.QUANTIDADE
    )

        quantidade.click()
        quantidade.clear()
        quantidade.send_keys(str(nova_quantidade))

    def delete_product(self):
        delete = self.driver.find_element(
            *self.DELETE
        )

        delete.click()

    def voltar_para_escolher_mais(self):
        shopping = self.driver.find_element(
            *self.CONTINUE_SHOPPING
        )

        shopping.click()

        
