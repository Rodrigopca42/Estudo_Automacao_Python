import logging
import os


def configurar_logger(pasta_execucao, nome_log="teste.log"):
    os.makedirs(pasta_execucao, exist_ok=True)

    caminho_log = os.path.join(
        pasta_execucao, nome_log
    )

    logging.basicConfig(
        filename=caminho_log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
        force=True
    )

    return logging.getLogger(__name__), caminho_log