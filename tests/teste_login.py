from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar o navegador
driver = webdriver.Chrome()

# Acessar a página de login
driver.get('https://hml-loja.spcbrasil.com.br/customer/account/login/referer/aHR0cHM6Ly9obWwtbG9qYS5zcGNicmFzaWwuY29tLmJyL3BhcmEtcGVzc29hcy1qdXJpZGljYXMvY29uc3VsdGE~/')

# Maximizar a tela
driver.maximize_window()

# Localizar o campo do usuário e preencher
campo_usurario = driver.find_element(By.ID, 'email')
campo_usurario.send_keys('53.416.790/0001-57')

# Localizar campo senha e preencher
campo_senha = driver.find_element(By.ID, 'password')
campo_senha.send_keys('Senha123$')

# Localizar e clicar no botão Entrar
btn_entrar = driver.find_element(By.XPATH, '//div[2]/button')

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable(btn_entrar)
)

btn_entrar.click()

# Aguardar alguns segundos para visualizar o resultado
time.sleep(10)

# fechar o navegador









