from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import logging
import os
from datetime import datetime

# ============================================================
# CONFIGURAÇÃO DE LOG
# ============================================================

os.makedirs('logs', exist_ok = True)

nome_log = datetime.now().strftime(
    'logs/teste_login_%Y%m%d_%H%M%S.log'
)

logging.basicConfig(
    filename=nome_log,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# ============================================================
# FUNÇÃO PARA CAPTURA DE EVIDÊNCIA
# ============================================================

def capturar_evidencia(driver, nome):
    os.makedirs('evidencias', exist_ok = True)

    caminho = f'evidencias/{nome}.png'

    sucesso = driver.save_screenshot(caminho)

    if sucesso:
       logger.info(f'Evidência capturada: {caminho}')
    else:
        logger.error(f'Falha ao capturar evidência: {caminho}')

# ============================================================
# INÍCIO DO TESTE
# ============================================================

# Inicializar o navegador
driver = webdriver.Chrome()

try:

    logger.info('==========INÍCIO DO TESTE DE LOGIN=============')

    # Acessar a página de login
    driver.get('https://hml-loja.spcbrasil.com.br/customer/account/login/referer/aHR0cHM6Ly9obWwtbG9qYS5zcGNicmFzaWwuY29tLmJyL3BhcmEtcGVzc29hcy1qdXJpZGljYXMvY29uc3VsdGE~/')

    # Maximizar a tela
    driver.maximize_window()

    logger.info('Página de login acessada')

    capturar_evidencia(
        driver, '01_pagina_login'
    )

    # ========================================================
    # PREENCHIMENTO DO USUÁRIO
    # ========================================================

    # Localizar o campo do usuário e preencher
    campo_usurario = driver.find_element(By.ID, 'email')
    campo_usurario.send_keys('53.416.790/0001-57')

    logger.info('Usuário preenchido')

    capturar_evidencia(
        driver, '02_usuário_preenchido'
    )

    # ========================================================
    # PREENCHIMENTO DA SENHA
    # ========================================================

    # Localizar campo senha e preencher
    campo_senha = driver.find_element(By.ID, 'password')
    campo_senha.send_keys('Senha123$')

    logger.info('Senha preenchida')

    capturar_evidencia(
        driver, '03_senha_preenchida'
    )

    # ========================================================
    # BOTÃO ENTRAR
    # ========================================================

    # Localizar e clicar no botão Entrar
    btn_entrar = driver.find_element(By.XPATH, '//div[2]/button.')

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(btn_entrar)
    )

    btn_entrar.click()

    logger.info('Botão Entrar clicado')

    capturar_evidencia(
        driver, '04_apos_login'
    )

    # ========================================================
    # FINALIZAÇÃO
    # ========================================================

    logger.info('Teste de login executado com sucesso')
    logger.info('===========FIM DO TESTE=============')


except Exception as erro:

    logger.error(
        f'Erro durente a execução do teste: {erro}'
    )

    capturar_evidencia(
        driver, 'Erro_login'
    )

    raise


finally:

    # fechar o navegador
    driver.quit()

    logger.info('Navegador encerrado')








