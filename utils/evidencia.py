import os






def capturar_evidencia(driver, pasta_execucao, nome):
    '''
    capturar uma evidência na tela e salva dentro da pasta da execução atual.
    '''
    os.makedirs(pasta_execucao, exist_ok=True)

    caminho = os.path.join(
        pasta_execucao, f'{nome}.png'
    )

    sucesso = driver.save_screenshot(caminho)

    if sucesso:
        return caminho


    return None
    