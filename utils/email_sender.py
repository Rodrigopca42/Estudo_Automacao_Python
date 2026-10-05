import os
import smtplib

from email.message import EmailMessage
from pathlib import Path


def enviar_relatorio_email(
    caminho_pdf,
    destinatario,
    assunto,
    corpo
):
    """
    Envia o relatório PDF por e-mail.

    As configurações SMTP são obtidas
    através das variáveis de ambiente.
    """

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "465"))
    smtp_usuario = os.getenv("SMTP_USUARIO")
    smtp_senha = os.getenv("SMTP_SENHA")

    if not smtp_host:
        raise ValueError(
            "A variável SMTP_HOST não foi configurada."
        )

    if not smtp_usuario:
        raise ValueError(
            "A variável SMTP_USUARIO não foi configurada."
        )

    if not smtp_senha:
        raise ValueError(
            "A variável SMTP_SENHA não foi configurada."
        )

    caminho_pdf = Path(caminho_pdf)

    if not caminho_pdf.exists():
        raise FileNotFoundError(
            f"Relatório não encontrado: {caminho_pdf}"
        )

    mensagem = EmailMessage()

    mensagem["From"] = smtp_usuario
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto

    mensagem.set_content(corpo)

    with open(caminho_pdf, "rb") as arquivo:
        mensagem.add_attachment(
            arquivo.read(),
            maintype="application",
            subtype="pdf",
            filename=caminho_pdf.name
        )

    with smtplib.SMTP_SSL(
        smtp_host,
        smtp_port
    ) as servidor:

        servidor.login(
            smtp_usuario,
            smtp_senha
        )

        servidor.send_message(mensagem)