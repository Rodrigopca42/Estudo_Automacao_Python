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