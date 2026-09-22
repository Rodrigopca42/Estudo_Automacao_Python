ID: CT-LOGIN-001

Feature: Login

Scenario: Login com credenciais válidas

Dado que acesso a página Home
Quando a página está completamente carregada
E clico no botão "Log in"
Então devo ser direcionado para página de login


Dado que estou na página de login
Quando informo um usuário válido
E informo uma senha válida
E clico no botão "Sign in"
Então devo ser autenticado com sucesso e enviado para Home