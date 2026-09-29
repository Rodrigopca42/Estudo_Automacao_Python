from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.configuracoes import TIMEOUT


class PdpPage:

    # ========================================================
    # ELEMENTOS GERAIS DA PDP
    # ========================================================

    IMAGE_PRODUCT = (By.XPATH, "//div[2]/section[1]/img[1]")
    DESCRIPTION = (By.XPATH, "//div[2]/section[3]/div")
    TITULO_PRODUCT = (By.XPATH, "//section[2]/form/h1")

    # ========================================================
    # ELEMENTOS DE PREÇO
    # ========================================================

    PRICE_PRODUCT_H2 = (By.XPATH, "//section[2]/form/h2")
    PRICE_PRODUCT_ID = (By.ID, "product-price")

    # ========================================================
    # OPÇÕES - BLACK HEELS
    # ========================================================

    BLACK_HEELS_SIZE = (
        By.XPATH,
        "//form/div[1]/div[1]/select"
    )

    BLACK_HEELS_COLOR = (
        By.XPATH,
        "//form/div[1]/div[2]/select"
    )

    # ========================================================
    # OPÇÕES - NOIR JACKET
    # ========================================================

    NOIR_JACKET_SIZE = (
        By.XPATH,
        "//form/div[1]/div[1]/select"
    )

    NOIR_JACKET_COLOR = (
        By.XPATH,
        "//form/div[1]/div[2]/select"
    )

    # ========================================================
    # OPÇÃO - GREY JACKET
    # ========================================================

    GREY_JACKET_FLAG = (
        By.XPATH,
        "//form/div[1]/div/select"
    )

    # ========================================================
    # ADD TO CART
    # ========================================================

    ADD_TO_CART = (
        By.XPATH,
        "//section[2]/form/input"
    )

    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(self, driver):
        self.driver = driver

    # ========================================================
    # HELPERS DE ELEMENTOS
    # ========================================================

    def localizar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def obter_texto(self, locator):
        elemento = self.localizar_elemento(locator)
        return elemento.text

    def elemento_visivel(self, locator):
        elemento = self.localizar_elemento(locator)
        return elemento.is_displayed()

    # ========================================================
    # HELPERS DE OPÇÕES
    # ========================================================

    def selecionar_opcao(self, locator, texto):
        elemento = self.localizar_elemento(locator)

        select = Select(elemento)
        select.select_by_visible_text(texto)

    def obter_opcoes(self, locator):
        elemento = self.localizar_elemento(locator)

        select = Select(elemento)

        return [
            opcao.text
            for opcao in select.options
        ]

    def obter_opcao_selecionada(self, locator):
        elemento = self.localizar_elemento(locator)

        select = Select(elemento)

        return select.first_selected_option.text

    # ========================================================
    # ADD TO CART
    # ========================================================

    def adicionar_ao_carrinho(self):

        botao_add_cart = self.localizar_elemento(
            self.ADD_TO_CART
        )

        ActionChains(self.driver).move_to_element(
            botao_add_cart
        ).perform()

        WebDriverWait(
            self.driver,
            TIMEOUT
        ).until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART
            )
        )

        botao_add_cart.click()