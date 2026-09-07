from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    TableStyle,
    PageBreak
)

import os

def ler_arquivo(caminho):
    '''
    Lê um arquivo de texto e retorna seu conteúdo.
    '''

    if not os.path.exists(caminho):
        return "Arquivo não encontrado."

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    except UnicodeDecodeError:

        with open(caminho, "r", encoding="cp1252") as arquivo:
            return arquivo.read()

def gerar_relatorio_pdf(
        id_execucao,
        caminho_cenario,
        pasta_evidencias,
        caminho_log,
        pasta_relatorio,
        status,
        ambiente = 'Homologação'
):
    '''
    Gera o relatório PDF da execução.

    O relatório contém:
    - Informações da execução
    - Cenário BDD
    - Screenshots
    - Log
    - Resultado
    '''
    os.makedirs(pasta_relatorio, exist_ok=True)

    caminho_pdf = os.path.join(
        pasta_relatorio,
        f'relatorio_{id_execucao}.pdf'
    )

    # ========================================================
    # CONFIGURAÇÃO DO DOCUMENTO
    # ========================================================
    
    documento = SimpleDocTemplate(
        caminho_pdf,
        pagesaze=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottonMargin=1.5 * cm 
    )

    estilos = getSampleStyleSheet()

    estilo_titulo = ParagraphStyle(
        'Título',
        parent=estilos['Title'],
        alignment=TA_CENTER,
        fontSize=18,
        spaceAfter=20
    )

    estilo_secao = ParagraphStyle(
        'Secao', 
        parent=estilos['Heading2'],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10
    )

    estilo_normal = ParagraphStyle(
        "Normal",
        parent=estilos["BodyText"],
        fontSize=10,
        leading=14
    )

    estilo_codigo = ParagraphStyle(
        "Codigo",
        parent=estilos["Code"],
        fontSize=8,
        leading=10
    )

    elementos = []

     # ========================================================
    # TÍTULO
    # ========================================================

    elementos.append(
        Paragraph(
            "RELATÓRIO DE EXECUÇÃO DE TESTES",
            estilo_titulo
        )
    )

    # ========================================================
    # INFORMAÇÕES DA EXECUÇÃO
    # ========================================================

    elementos.append(
        Paragraph(
            "Informações da execução",
            estilo_secao
        )
    )

    dados_execucao = [
        ["ID da execução", id_execucao],
        ["Ambiente", ambiente],
        ["Status", status]
    ]

    tabela_execucao = Table(
        dados_execucao,
        colWidths=[5 * cm, 11 * cm]
    )

    tabela_execucao.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("PADDING", (0, 0), (-1, -1), 6)
        ])
    )

    elementos.append(tabela_execucao)

    elementos.append(Spacer(1, 15))

    # ========================================================
    # CENÁRIO BDD
    # ========================================================

    elementos.append(
        Paragraph(
            "Cenário de teste BDD",
            estilo_secao
        )
    )

    cenario = ler_arquivo(caminho_cenario)

    # Escapa caracteres que poderiam ser interpretados
    # pelo ReportLab como HTML.
    cenario = (
        cenario
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )

    elementos.append(
        Paragraph(
            cenario,
            estilo_codigo
        )
    )

    elementos.append(PageBreak())

    # ========================================================
    # EVIDÊNCIAS
    # ========================================================

    elementos.append(
        Paragraph(
            "Evidências da execução",
            estilo_secao
        )
    )

    if os.path.exists(pasta_evidencias):

        imagens = sorted(
            arquivo
            for arquivo in os.listdir(pasta_evidencias)
            if arquivo.lower().endswith(
                (".png", ".jpg", ".jpeg")
            )
        )

        if imagens:

            for imagem in imagens:

                caminho_imagem = os.path.join(
                    pasta_evidencias,
                    imagem
                )

                elementos.append(
                    Paragraph(
                        f"Evidência: {imagem}",
                        estilo_normal
                    )
                )

                img = Image(
                    caminho_imagem,
                    width=16 * cm,
                    height=9 * cm
                )

                elementos.append(img)

                elementos.append(
                    Spacer(1, 15)
                )

        else:

            elementos.append(
                Paragraph(
                    "Nenhuma evidência encontrada.",
                    estilo_normal
                )
            )

    else:

        elementos.append(
            Paragraph(
                "Pasta de evidências não encontrada.",
                estilo_normal
            )
        )

    elementos.append(PageBreak())

    # ========================================================
    # LOG
    # ========================================================

    elementos.append(
        Paragraph(
            "Log da execução",
            estilo_secao
        )
    )

    log = ler_arquivo(caminho_log)

    log = (
        log
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )

    elementos.append(
        Paragraph(
            log,
            estilo_codigo
        )
    )

    elementos.append(Spacer(1, 20))

    # ========================================================
    # RESULTADO
    # ========================================================

    elementos.append(
        Paragraph(
            "Resultado da execução",
            estilo_secao
        )
    )

    elementos.append(
        Paragraph(
            f"<b>Status:</b> {status}",
            estilo_normal
        )
    )

    # ========================================================
    # GERAR PDF
    # ========================================================

    documento.build(elementos)

    return caminho_pdf