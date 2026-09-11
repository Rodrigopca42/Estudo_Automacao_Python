from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from datetime import datetime

from utils.evidencia import capturar_evidencia
from utils.logger import configurar_logger
from utils.relatorio_pdf import gerar_relatorio_pdf

from config.configuracoes import (
    URL_LOGIN,
    USUARIO_TESTE,
    SENHA_TESTE,
    TIMEOUT,
    AMBIENTE
)

# ============================================================
# IDENTIFICAÇÃO DA EXECUÇÃO
# ============================================================

id_execucao = datetime.now().strftime(
    '%Y-%m-%d_%H-%M-%S'
)

# ============================================================
# PASTAS DA EXECUÇÃO
# ============================================================

pasta_evidencia = os.path.join(
    'evidências', id_execucao
)

pasta_logs = os.path.join(
    'logs', id_execucao
)

pasta_relatorio = os.path.join(
    'reports', id_execucao
)

#criar pastas
os.makedirs(pasta_evidencia, exist_ok=True)
os.makedirs(pasta_logs, exist_ok=True)
os.makedirs(pasta_relatorio, exist_ok=True)



# ============================================================
# CONFIGURAÇÃO DE LOG
# ============================================================

logger = configurar_logger(pasta_logs)


# ============================================================
# CAMINHO DO CENÁRIO BDD
# ============================================================

caminho_cenario = os.path.join(
    "cenarios",
    "CT-LOGIN-001.md"
)

# ============================================================
# VARIÁVEIS DO TESTE
# ============================================================

status_teste = "FAIL"
caminho_log = os.path.join(
    pasta_logs,
    "teste_login.log"
)

driver = None

# ============================================================
# INÍCIO DO TESTE
# ============================================================

# Inicializar o navegador
driver = webdriver.Chrome()

try:

    logger.info('==========INÍCIO DO TESTE DE LOGIN=============')

    # Acessar a página de login
    driver.get(URL_LOGIN)

    # Maximizar a tela
    driver.maximize_window()

    logger.info('Página de login acessada')

    capturar_evidencia(
        driver,
        pasta_evidencia,
        '01_pagina_login'
    )

    # ========================================================
    # PREENCHIMENTO DO USUÁRIO
    # ========================================================

    # Localizar o campo do usuário e preencher
    campo_usurario = driver.find_element(By.ID, 'email')
    campo_usurario.send_keys(USUARIO_TESTE)

    logger.info('Usuário preenchido')

    capturar_evidencia(
        driver,
        pasta_evidencia,
        '02_usuário_preenchido'
    )

    # ========================================================
    # PREENCHIMENTO DA SENHA
    # ========================================================

    # Localizar campo senha e preencher
    campo_senha = driver.find_element(By.ID, 'password')
    campo_senha.send_keys(SENHA_TESTE)

    logger.info('Senha preenchida')

    capturar_evidencia(
        driver, 
        pasta_evidencia,
        '03_senha_preenchida'
    )

    # ========================================================
    # BOTÃO ENTRAR
    # ========================================================

    # Localizar e clicar no botão Entrar
    btn_entrar = driver.find_element(By.XPATH, '//div[2]/button')

    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(btn_entrar)
    )

    btn_entrar.click()

    logger.info('Botão Entrar clicado')

    capturar_evidencia(
        driver,
        pasta_evidencia,
        '04_apos_login'
    )

    # ========================================================
    # TESTE APROVADO
    # ========================================================

    status_teste = "PASS"

    logger.info(
        "Teste de login executado com sucesso"
    )

    # ========================================================
    # FINALIZAÇÃO
    # ========================================================

    logger.info('Teste de login executado com sucesso')
    logger.info('===========FIM DO TESTE=============')


except Exception as erro:

    # ========================================================
    # TESTE REPROVADO
    # ========================================================

    status_teste = "FAIL"

    logger.error(
        f'Erro durante a execução do teste: {erro}'
    )

    if driver is not None:

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "erro_login"
        )

    raise


finally:

    # ========================================================
    # ENCERRAR NAVEGADOR
    # ========================================================

    if driver is not None:

        driver.quit()

        logger.info(
            "Navegador encerrado"
        )

    logger.info(
        "=========== FIM DO TESTE ==========="
    )

    # ========================================================
    # GERAR RELATÓRIO PDF
    # ========================================================

    caminho_pdf = gerar_relatorio_pdf(
        id_execucao=id_execucao,
        caminho_cenario=caminho_cenario,
        pasta_evidencias=pasta_evidencia,
        caminho_log=caminho_log,
        pasta_relatorio=pasta_relatorio,
        status=status_teste,
        ambiente=AMBIENTE
    )

    print(
        f"\nRelatório PDF gerado em: {caminho_pdf}"
    )




