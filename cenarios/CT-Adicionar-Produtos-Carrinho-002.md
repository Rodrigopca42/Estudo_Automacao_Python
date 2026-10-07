Cenário: Adicionar produtos ao carrinho

Como um usuário
Quero adicionar um ou mais produtos ao carrinho
Para validar se o produto e suas informações persistem no carrinho

Dado que o usuário possui acesso ao site
Quando o usuário acessa a Home
E clica na opção "catálogo" no navbar
Então o usuário é direcionado para a página Catálogo

Dado que o usuário acessou a página Catálogo
Quando o usuário seleciona um produto do 1ª step
E é direcionado para a PDP do produto
Então clica no btn “ADD TO CART”
E o produto é adicionado ao carrinho

Dado que o usuário retorna para o Catálogo
Quando o usuário seleciona um produto do 2ª step
E é direcionado para a PDP do produto
Então clica no btn “ADD TO CART”
E o produto é adicionado ao carrinho

Dado que o usuário retorna para o Home
Quando o usuário clica no minicar no header
Então o carrinho abre
E verifica se os produtos disponíveis lá são os produtos escolhidos nos passos anteriores.
