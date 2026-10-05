import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()


SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
SMTP_USUARIO = os.getenv("SMTP_USUARIO")
SMTP_SENHA = os.getenv("SMTP_SENHA")
EMAIL_DESTINATARIO = os.getenv("EMAIL_DESTINATARIO")


mensagem = EmailMessage()

mensagem["From"] = SMTP_USUARIO
mensagem["To"] = EMAIL_DESTINATARIO
mensagem["Subject"] = "Teste de envio - Automação Python"

mensagem.set_content(
    "Olá!\n\n"
    "Este é um teste de envio de e-mail "
    "da automação Python/Pytest/Selenium.\n\n"
    "Se você recebeu esta mensagem, "
    "a configuração SMTP está funcionando corretamente."
)


with smtplib.SMTP_SSL(
    SMTP_HOST,
    SMTP_PORT
) as servidor:

    servidor.login(
        SMTP_USUARIO,
        SMTP_SENHA
    )

    servidor.send_message(mensagem)


print("E-mail enviado com sucesso.")