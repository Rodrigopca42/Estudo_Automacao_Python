
import os
from datetime import datetime

from utils.evidencia import capturar_evidencia
from utils.logger import configurar_logger
from utils.relatorio_pdf import gerar_relatorio_pdf

from config.configuracoes import *

from pages.header_page import HeaderPage
from pages.login_page import LoginPage

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

# ============================================================
# INÍCIO DO TESTE
# ============================================================

def test_login(navegador):

     # Acessar a página de login
    driver = navegador

    status_teste = "FAIL"

    try:

        logger.info('==========INÍCIO DO TESTE DE LOGIN=============')

        # Maximizar a tela
        driver.maximize_window()

        
        # ========================================================
        # ACESSANDO A HOME
        # ========================================================

        logger.info('Página HOME acessada')
        
        capturar_evidencia(
            driver,
            pasta_evidencia,
            '01_pagina_home'
        )

        header = HeaderPage(driver)
        login = LoginPage(driver)


        header.acessar_login()

        # ========================================================
        # ACESSANDO A PAGINA LOGIN
        # ========================================================

        logger.info('Página de login acessada')

        capturar_evidencia(
            driver,
            pasta_evidencia,
            '02_pagina_login'
        )

        # ========================================================
        # PREENCHIMENTO DO USUÁRIO
        # ========================================================

        # Localizar o campo do usuário e preencher
        login.preencher_usuario(USUARIO_TESTE)

        logger.info('Usuário preenchido')

        capturar_evidencia(
            driver,
            pasta_evidencia,
            '03_usuário_preenchido'
        )

        # ========================================================
        # PREENCHIMENTO DA SENHA
        # ========================================================

        # Localizar campo senha e preencher
        login.preencher_senha(SENHA_TESTE)

        logger.info('Senha preenchida')

        capturar_evidencia(
            driver, 
            pasta_evidencia,
            '04_senha_preenchida'
        )

        # ========================================================
        # BOTÃO ENTRAR
        # ========================================================

        # Localizar e clicar no botão Entrar
        login.clicar_entrar()

        logger.info('Botão Entrar clicado')

        capturar_evidencia(
            driver,
            pasta_evidencia,
            '05_clique no botão'
        )
        
        # ========================================================
        # TESTE APROVADO
        # ========================================================

        status_teste = "PASS"


        # ========================================================
        # FINALIZAÇÃO
        # ========================================================

        logger.info('Teste de login executado com sucesso')
        logger.info('===========FIM DO TESTE=============')


    except Exception as erro:

        # ========================================================
        # TESTE REPROVADO
        # ========================================================

        

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




