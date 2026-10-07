from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config.configuracoes import (
    TIMEOUT,
    TEMPO_ATUALIZACAO_MINICART
)

class HeaderPage:

    # ========================================================
    # LOCATORS
    # ========================================================

    INPUT_SEARCH = (By.ID, "search-field")
    SEARCH_SUBMIT = (By.ID, "search-submit")
    ABOUT_US = (By.XPATH, "/header/div[1]/div[2]/nav/a[2]")
    LOGIN = (By.XPATH, "//div[2]/nav/a[3]")
    SIGN_UP = (By.XPATH, "//div[2]/nav/a[4]")
    MINI_CART = (By.XPATH, "//div[1]/div[3]/div/a[1]")
    MINI_CART_QUANTIDADE = (By.XPATH, "//div[3]/div/a[1]/span")
    CHECK_OUT = (By.XPATH, '//*[@id="minicart"]/a[3]')
    LOGOTIPO = (By.XPATH, '//*[@id="logo"]/a/img')

    # ========================================================
    # CONSTRUTOR
    # ========================================================

    def __init__(self, driver):
        self.driver = driver

    # ========================================================
    # AÇÕES
    # ========================================================

    def pesquisar(self, texto):
        campo_busca = self.driver.find_element(
            *self.INPUT_SEARCH
        )

        campo_busca.send_keys(texto)

    def executar_busca(self):
        botao_busca = self.driver.find_element(
            *self.SEARCH_SUBMIT
        )

        botao_busca.click()

    def acessar_login(self):
        botao_login = self.driver.find_element(
            *self.LOGIN
        )

        botao_login.click()

    def acessar_cadastro(self):
        botao_cadastro = self.driver.find_element(
            *self.SIGN_UP
        )

        botao_cadastro.click()

    def acessar_sobre_nos(self):
        link_sobre_nos = self.driver.find_element(
            *self.ABOUT_US
        )

        link_sobre_nos.click()

    def acessar_mini_carrinho(self):
        mini_cart = self.driver.find_element(
            *self.MINI_CART
        )

        mini_cart.click()


    def aguardar_quantidade_minicart(self, quantidade):
        WebDriverWait(
        self.driver,
        TEMPO_ATUALIZACAO_MINICART
    ).until(
        lambda driver: driver.find_element(
            *self.MINI_CART_QUANTIDADE
        ).text.strip() == str(quantidade)
    )
    
    def acessar_checkout(self):
        checkout = self.driver.find_element(
            *self.CHECK_OUT
        )

        checkout.click()

    def acessar_logo(self):
        logo = self.driver.find_element(
            *self.LOGOTIPO
        )

        logo.click()