ID: CT-LOGIN-001

Feature: Login

Scenario: Login com credenciais válidas

Dado que estou na página de login
Quando informo um usuário válido
E informo uma senha válida
E clico no botão "Entrar"
Então devo ser autenticado com sucesso e enviado para Home