import logging
import os


def configurar_logger(pasta_execucao):
    os.makedirs(pasta_execucao, exist_ok=True)

    caminho_log = os.path.join(
        pasta_execucao, 'teste_login.log'
    )

    logging.basicConfig(
        filename=caminho_log,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True
    )

    return logging.getLogger(__name__)