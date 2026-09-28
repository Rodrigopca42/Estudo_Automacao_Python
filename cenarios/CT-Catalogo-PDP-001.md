ID: CT-CATALOGO-PDP-001

Feature: Catálogo e visualização de produto

Scenario: Acessar o catálogo e visualizar os detalhes de um produto

Dado que o usuário acessa a página Home
Quando o usuário acessa a opção "Catálogo"
Então a página de catálogo deve ser apresentada
E os produtos disponíveis devem ser apresentados

Quando o usuário seleciona o produto "Grey Jacket"
Então a página de detalhes do produto deve ser apresentada
E o produto selecionado deve ser apresentado

Quando o usuário aciona a opção "ADD TO CART"
Então o produto deve ser adicionado ao carrinho