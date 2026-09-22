import pytest
from selenium import webdriver
from config.configuracoes import *

@pytest.fixture

def navegador():
    driver = webdriver.Chrome()
    driver.get(URL_HOME)

    yield driver

    driver.quit()



