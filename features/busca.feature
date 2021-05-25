#Language: pt

Funcionalidade: fluxo de busca

  @busca
  Cenário: realizar busca
    Dado que da acesso ao site Petz
    E preencho o input de pesquisa
    Quando clico no botão de pesquisar
    Então traz o retorno de minha pesquisa
    Quando validação do fornecedor
    Então validação do preço do produto
    Então validação do preço para assinante
