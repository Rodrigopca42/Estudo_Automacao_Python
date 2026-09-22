

import os
from dotenv import load_dotenv

load_dotenv()


URL_LOGIN = "https://sauce-demo.myshopify.com/account/login"

URL_HOME = 'https://sauce-demo.myshopify.com/'

AMBIENTE = "Homologação"

TIMEOUT = 5

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