  Sistema de Gestão de Inventário GLT Veículos

O sistema permite ao usuário:

Cadastrar informações iniciais (nome, telefone, saldo).

Visualizar o inventário de veículos.

Realizar transações de venda, aluguel e compra de novos veículos para o estoque.

O programa iniciará solicitando o cadastro inicial.

1. Configuração Inicial e Variáveis Globais

As seguintes variáveis são usadas para configurar o estado inicial do sistema e do cliente:

Variável

Tipo

Descrição

cliente_name

str

Armazena o nome do cliente.

cliente_number

str

Armazena o telefone de contato do cliente.

saldoFinal

float

Saldo inicial do cliente para transações.

inventory

list

O banco de dados principal do sistema. É uma lista de dicionários, onde cada dicionário representa um veículo.

2. Estrutura de Dados (inventory)

A lista inventory contém veículos pré-cadastrados (SUVs, Sedans, Motos, Caminhonetes).

Formato de um Veículo (Dicionário):

id: Código único do veículo (ex: "SUV001").

categoria: Tipo de veículo (ex: "SUV", "Sedan").

marca: Marca do veículo.

modelo: Modelo do veículo.

ano: Ano de fabricação.

preco: Preço de venda/inventário do veículo (em R$).

status: Condição atual ("disponivel").

3. Funções (Ações do Sistema)

menu()

Descrição: Exibe o menu de opções disponíveis e o saldo atual do cliente.

buscar_por_id(vid)

Descrição: Procura e retorna um veículo na lista inventory usando o ID (vid). Retorna None se não for encontrado.

lista_veiculos()

Descrição: Imprime todos os veículos do inventário em um formato de lista formatada.

comprar_veiculo(saldo)

Descrição: Permite ao cliente adicionar (comprar) um novo veículo para o inventário da GLT

Lógica de Preço: O preço de inventário é o Preço Base + 25% de acréscimo.

vender_veiculo(saldo)

Descrição: Simula a venda de um veículo do inventário para um cliente externo.

Lógica de Preço: O valor da venda é o Preço de Inventário - 12% de desconto. O valor da venda é adicionado ao saldoFinal.

alugar_veiculo(saldo)

Descrição: Permite ao cliente alugar um veículo. O veículo é removido do inventário e o valor é descontado do saldo.

Lógica de Preço: O custo é fixo em R$ 159,00 por dia.

4. Loop Principal do Programa

O sistema opera em um loop contínuo que exibe o menu e processa a opção escolhida pelo usuário, utilizando a estrutura match case. O programa é encerrado ao selecionar a opção 0 (SAIR).
