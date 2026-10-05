import os
from datetime import datetime

from utils.evidencia import *
from utils.logger import configurar_logger
from utils.relatorio_pdf import gerar_relatorio_pdf

from config.configuracoes import *

from pages.navbar_page import NavBarPage
from pages.catalog_page import CatalogPage
from pages.pdp_page import PdpPage

from utils.email_sender import enviar_relatorio_email


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
    'evidências',
    id_execucao
)

pasta_execucao = os.path.join(
    "logs",
    id_execucao
)


pasta_relatorio = os.path.join(
    'reports',
    id_execucao
)

os.makedirs(pasta_evidencia, exist_ok=True)
os.makedirs(pasta_execucao, exist_ok=True)
os.makedirs(pasta_relatorio, exist_ok=True)


# ============================================================
# CONFIGURAÇÃO DE LOG
# ============================================================

logger, caminho_log = configurar_logger(
    pasta_execucao,
    "teste_catalogo_pdp.log"
)


# ============================================================
# CENÁRIO BDD
# ============================================================

caminho_cenario = os.path.join(
    "cenarios",
    "CT-CATALOGO-PDP-001.md"
)


# ============================================================
# VARIÁVEIS DO TESTE
# ============================================================

status_teste = "FAIL"

caminho_log = os.path.join(
    pasta_execucao,
    "teste_catalogo_pdp.log"
)


# ============================================================
# TESTE
# ============================================================

def test_acessar_catalogo_e_visualizar_produto(navegador):

    driver = navegador

    status_teste = "FAIL"

    try:

        logger.info(
            '=== INÍCIO DO TESTE DE CATÁLOGO E PDP ==='
        )

        driver.maximize_window()

        logger.info('Home com navbar, clicar na opção catalogo')
        
        capturar_evidencia(
            driver,
            pasta_evidencia,
            '01_Home'
        )

        # ====================================================
        # ACESSAR CATÁLOGO
        # ====================================================

        navbar = NavBarPage(driver)

        navbar.acessar_catalogo()

        logger.info('Catálogo acessado')

        capturar_evidencia(
            driver,
            pasta_evidencia,
            '02_catalogo'
        )

        # ====================================================
        # SELECIONAR PRODUTO
        # ====================================================

        catalogo = CatalogPage(driver)

        catalogo.rolar_para_step_2()

        logger.info(
            'Produto Grey Jacket localizado na PLP'
        )

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            '03_grey_jacket_na_plp',
            catalogo.CARD_GREY_JACKET_COMPLET
        )

        # ====================================================
        # ACESSAR PDP
        # ====================================================

        catalogo.acessar_produto(
            catalogo.CARD_GREY_JACKET_COMPLET
        )

        logger.info(
            'Produto selecionado: Grey Jacket'
        )

        capturar_evidencia(
            driver,
            pasta_evidencia,
            '04_pdp'
        )

        # ====================================================
        # ADD TO CART
        # ====================================================

        pdp = PdpPage(driver)

        pdp.adicionar_ao_carrinho()

        logger.info(
            'ADD TO CART acionado'
        )

        capturar_evidencia(
            driver,
            pasta_evidencia,
            '05_add_to_cart'
        )

        # ====================================================
        # FINALIZAÇÃO
        # ====================================================

        status_teste = "PASS"

        logger.info(
            'Teste executado com sucesso'
        )

        logger.info(
            '========== FIM DO TESTE =========='
        )

    except Exception as erro:

        logger.error(
            f'Erro durante a execução do teste: {erro}'
        )

        if driver is not None:

            capturar_evidencia(
                driver,
                pasta_evidencia,
                'erro_catalogo_pdp'
            )

        raise

    finally:

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

        enviar_relatorio_email(
            caminho_pdf=caminho_pdf,
            destinatario=EMAIL_DESTINATARIO,
            assunto=(
                f"Relatório de execução - "
                f"{status_teste} - "
                f"{id_execucao}"
            ),
            corpo=(
                "Olá,\n\n"
                "Segue em anexo o relatório da execução "
                "automatizada de testes.\n\n"
                f"ID da execução: {id_execucao}\n"
                f"Ambiente: {AMBIENTE}\n"
                f"Status: {status_teste}\n\n"
                "Relatório gerado automaticamente."
            )
        )