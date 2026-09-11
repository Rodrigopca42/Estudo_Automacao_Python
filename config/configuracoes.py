

import os
from dotenv import load_dotenv

load_dotenv()


URL_LOGIN = "https://hml-loja.spcbrasil.com.br/customer/account/login/referer/aHR0cHM6Ly9obWwtbG9qYS5zcGNicmFzaWwuY29tLmJyL3BhcmEtcGVzc29hcy1qdXJpZGljYXMvY29uc3VsdGE~/"

AMBIENTE = "Homologação"

TIMEOUT = 1

USUARIO_TESTE = os.getenv('USUARIO_TESTE')
if not USUARIO_TESTE:
    raise ValueError(
        'A variável USUARIO_TESTE não foi configurada no arquivo .env'
    )

SENHA_TESTE = os.getenv('SENHA_TESTE')
if not SENHA_TESTE:
    raise ValueError(
        'A variável SENHA_TESTE não foi configurada no arquivo .env'
    )