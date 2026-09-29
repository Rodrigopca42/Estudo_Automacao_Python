import os
import time

from config.configuracoes import TEMPO_ESPERA_EVIDENCIA


def aguardar_carregamento():
    time.sleep(TEMPO_ESPERA_EVIDENCIA)


def capturar_evidencia(driver, pasta_execucao, nome):
    os.makedirs(pasta_execucao, exist_ok=True)

    aguardar_carregamento()

    caminho = os.path.join(
        pasta_execucao,
        f"{nome}.png"
    )

    sucesso = driver.save_screenshot(caminho)

    if sucesso:
        return caminho

    return None


def capturar_evidencia_destacada(
    driver,
    pasta_execucao,
    nome,
    locator
):
    os.makedirs(pasta_execucao, exist_ok=True)

    destacar_elemento(driver, locator)

    aguardar_carregamento()

    caminho = os.path.join(
        pasta_execucao,
        f"{nome}.png"
    )

    sucesso = driver.save_screenshot(caminho)

    if sucesso:
        return caminho

    return None


def destacar_elemento(driver, locator):
    elemento = driver.find_element(*locator)

    driver.execute_script(
        """
        arguments[0].style.border = '3px solid green';
        arguments[0].style.boxSizing = 'border-box';
        """,
        elemento
    )