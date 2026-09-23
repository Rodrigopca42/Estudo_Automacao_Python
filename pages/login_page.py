from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def preencher_usuario(self, usuario):
        campo_usuario = self.driver.find_element(
            By.ID,
            'customer_email'
        )

        campo_usuario.send_keys(usuario)

    def preencher_senha(self, senha):
        campo_senha = self.driver.find_element(
            By.ID,
            'customer_password'
        )

        campo_senha.send_keys(senha)

    def clicar_entrar(self):
        btn_entrar = self.driver.find_element(
            By.XPATH,
            '//div[5]/input'
        )

        btn_entrar.click()