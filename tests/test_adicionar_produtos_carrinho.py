import os
from datetime import datetime

from utils.evidencia import *
from utils.logger import configurar_logger
from utils.relatorio_pdf import gerar_relatorio_pdf
from utils.email_sender import enviar_relatorio_email

from config.configuracoes import *

from pages.navbar_page import NavBarPage
from pages.header_page import HeaderPage
from pages.catalog_page import CatalogPage
from pages.pdp_page import PdpPage
from pages.cart_page import CartPage


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
    "evidências",
    id_execucao
)

pasta_execucao = os.path.join(
    "logs",
    id_execucao
)

pasta_relatorio = os.path.join(
    "reports",
    id_execucao
)

os.makedirs(pasta_evidencia, exist_ok=True)
os.makedirs(pasta_execucao, exist_ok=True)
os.makedirs(pasta_relatorio, exist_ok=True)


# ============================================================
# CONFIGURAÇÃO DO LOG
# ============================================================

logger, caminho_log = configurar_logger(
    pasta_execucao,
    "teste_adicionar_produtos_carrinho.log"
)


# ============================================================
# CENÁRIO BDD
# ============================================================

caminho_cenario = os.path.join(
    "cenarios",
    "CT-Adicionar-Produtos-Carrinho-002.md"
)


# ============================================================
# TESTE
# ============================================================

def test_adicionar_produtos_ao_carrinho(navegador):

    driver = navegador

    status_teste = "FAIL"

    try:

        logger.info(
            "========== INÍCIO DO TESTE: ADICIONAR PRODUTOS AO CARRINHO =========="
        )

        driver.maximize_window()

        # ====================================================
        # HOME
        # ====================================================

        logger.info("Home acessada")

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "01_Home"
        )

        # ====================================================
        # ACESSAR CATÁLOGO
        # ====================================================

        logger.info(
            "Clique em Catálogo na navbar"
        )

        navbar = NavBarPage(driver)
        header = HeaderPage(driver)

        navbar.acessar_catalogo()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "02_catalogo"
        )

        # ====================================================
        # PRODUTO 1 - STEP 1
        # ====================================================

        logger.info(
            "Selecionando o primeiro produto no catálogo"
        )

        catalogo = CatalogPage(driver)

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "03_produto_1_plp",
            catalogo.CARD_BLACK_HEELS_COMPLET
        )

        catalogo.acessar_produto(
            catalogo.CARD_BLACK_HEELS_COMPLET
        )

        # ====================================================
        # PDP - PRODUTO 1
        # ====================================================

        logger.info(
            "PDP do primeiro produto acessada"
        )

        pdp = PdpPage(driver)

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "04_produto_1_pdp",
            pdp.ADD_TO_CART
        )

        pdp.adicionar_ao_carrinho()

        # ====================================================
        # MINICART - PRODUTO 1
        # ====================================================

        logger.info(
    "Primeiro produto adicionado ao minicart"
    )

        aguardar_atualizacao_minicart()

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "05_produto_1_minicart",
            header.MINI_CART
        )
        # ====================================================
        # RETORNO AO CATÁLOGO
        # ====================================================

        logger.info(
            "Retorno ao catálogo"
        )

        navbar.acessar_catalogo()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "06_retorno_catalogo"
        )

        # ====================================================
        # PRODUTO 2 - STEP 2
        # ====================================================

        logger.info(
            "Selecionando outro produto no segundo step"
        )

        catalogo.rolar_para_step_2()

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "07_produto_2_plp",
            catalogo.CARD_GREY_JACKET_COMPLET
        )

        catalogo.acessar_produto(
            catalogo.CARD_GREY_JACKET_COMPLET
        )

        # ====================================================
        # PDP - PRODUTO 2
        # ====================================================

        logger.info(
            "PDP do segundo produto acessada"
        )

        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "08_produto_2_pdp",
            pdp.ADD_TO_CART
        )

        pdp.adicionar_ao_carrinho()

        # ====================================================
        # MINICART - PRODUTO 2
        # ====================================================

        logger.info(
            "Segundo produto adicionado ao minicart"
        )

        aguardar_atualizacao_minicart()
        
        capturar_evidencia_destacada(
            driver,
            pasta_evidencia,
            "09_produto_2_minicart",
            header.MINI_CART
        )

        # ====================================================
        # RETORNO AO CATÁLOGO
        # ====================================================

        logger.info(
            "Retorno ao catálogo"
        )

        navbar.acessar_catalogo()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "10_retorno_catalogo"
        )

       # ====================================================
       # VERIFICAR PRODUTOS NO MINICART
       # ====================================================

        logger.info(
            "Acessando minicart para verificar os produtos"
        )

        header.acessar_mini_carrinho()

        cart = CartPage(driver)

        cart.destacar_produto_1()
        cart.destacar_produto_2()

        capturar_evidencia(
            driver,
            pasta_evidencia,
            "11_produtos_no_carrinho"
        )

        # ====================================================
        # FINALIZAÇÃO
        # ====================================================

        logger.info(
            "Produtos verificados no minicart"
        )

        status_teste = "PASS"

        logger.info(
            "Sucesso"
        )

        logger.info(
            "========== FIM DO TESTE =========="
        )
    except Exception as erro:

        logger.error(
            f"Erro durante a execução do teste: {erro}"
        )

        if driver is not None:

            capturar_evidencia(
                driver,
                pasta_evidencia,
                "erro_adicionar_produtos_carrinho"
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

        # ========================================================
        # ENVIO DO RELATÓRIO POR E-MAIL
        # ========================================================

        email_destinatario = os.getenv(
            "EMAIL_DESTINATARIO"
        )

        if not email_destinatario:
            raise ValueError(
                "A variável EMAIL_DESTINATARIO não foi configurada."
            )

        enviar_relatorio_email(
            caminho_pdf=caminho_pdf,
            destinatario=email_destinatario,
            assunto=(
                f"Relatório de Automação - "
                f"Adicionar Produtos ao Carrinho - "
                f"{status_teste}"
            ),
            corpo=(
                f"Olá,\n\n"
                f"Segue em anexo o relatório da execução "
                f"do teste 'Adicionar Produtos ao Carrinho'.\n\n"
                f"Status: {status_teste}\n"
                f"Ambiente: {AMBIENTE}\n"
                f"Execução: {id_execucao}\n\n"
                f"Relatório gerado automaticamente."
            )
        )

        print(
            f"E-mail enviado para: {email_destinatario}"
        )