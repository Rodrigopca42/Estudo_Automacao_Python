import pytest
from selenium import webdriver
from config.configuracoes import *

@pytest.fixture

def navegador():
    driver = webdriver.Chrome()
    driver.get(URL_HOME)

    yield driver

    driver.quit()

'''
@pytest.fixture

def url_home(URL_HOME):
   return URL_HOME
'''

