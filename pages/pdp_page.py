from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.configuracoes import TIMEOUT


class PdpPage:

    # ========================================================
    # LOCATORS
    # ========================================================

    ADD_TO_CART = (By.ID, "add")

    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(self, driver):
        self.driver = driver

    # ========================================================
    # AÇÕES
    # ========================================================

    def adicionar_ao_carrinho(self):

        botao_add_cart = self.driver.find_element(
            *self.ADD_TO_CART
        )

        ActionChains(self.driver).move_to_element(
            botao_add_cart
        ).perform()

        WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(self.ADD_TO_CART)
        )

        botao_add_cart.click()