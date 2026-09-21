from config.configuracoes import URL_LOGIN


def teste_o_navegador(navegador):
    navegador.get(URL_LOGIN)

    navegador.maximize_window()
    
    assert navegador == WebDriver()

