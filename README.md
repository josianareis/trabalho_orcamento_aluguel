# Sistema de Orçamento de Aluguel

Projeto desenvolvido para a disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming**, do curso de Análise e Desenvolvimento de Sistemas da UNIFECAF.

A aplicação simula a geração de orçamentos para a imobiliária R.M., considerando diferentes tipos de imóveis, características adicionais, desconto, contrato imobiliário e planejamento de 12 mensalidades.

## Objetivo

Automatizar a elaboração de orçamentos de aluguel para apartamentos, casas e estúdios, apresentando o valor mensal, o parcelamento do contrato imobiliário e o planejamento financeiro dos 12 primeiros meses.

## Funcionalidades

- Cadastro do nome do cliente.
- Seleção do tipo de imóvel.
- Seleção da quantidade de quartos.
- Inclusão de garagem.
- Aplicação de desconto para apartamentos.
- Seleção de vagas para estúdios.
- Parcelamento do contrato entre 1 e 5 vezes.
- Cálculo automático do aluguel mensal.
- Apresentação do planejamento dos 12 meses.
- Geração de arquivo CSV compatível com o Excel.
- Validação de campos obrigatórios e valores inválidos.

## Regras de negócio

### Apartamento

- Valor-base: R$ 700,00.
- Segundo quarto: acréscimo de R$ 200,00.
- Garagem: acréscimo de R$ 300,00.
- Cliente sem crianças: desconto de 5% no aluguel.

### Casa

- Valor-base: R$ 900,00.
- Segundo quarto: acréscimo de R$ 250,00.
- Garagem: acréscimo de R$ 300,00.

### Estúdio

- Valor-base: R$ 1.200,00.
- Pacote inicial com duas vagas: acréscimo de R$ 250,00.
- Cada vaga depois das duas primeiras: acréscimo de R$ 60,00.
- O estúdio pode possuir zero vaga ou, no mínimo, duas vagas.

### Contrato imobiliário

- Valor fixo: R$ 2.000,00.
- Parcelamento permitido: de 1 a 5 vezes.
- As parcelas do contrato são somadas ao aluguel nos meses correspondentes.
- Depois do término do parcelamento, o cliente paga somente o aluguel mensal.

## Tecnologias utilizadas

- Python 3
- Tkinter
- Módulo CSV
- Visual Studio Code
- Git e GitHub

A aplicação utiliza somente recursos da biblioteca padrão do Python, não sendo necessária a instalação de dependências externas.

## Conceitos aplicados

O projeto utiliza os seguintes conceitos de programação:

- Classes e objetos
- Atributos e métodos
- Herança
- Polimorfismo
- Composição
- Encapsulamento
- Estruturas condicionais
- Estruturas de repetição
- Listas e dicionários
- Tratamento de exceções
- Manipulação de arquivos CSV
- Interface gráfica orientada a eventos

## Estrutura do projeto

```text
trabalho_orcamento_aluguel/
├── .gitignore
├── exemplo_orcamento.csv
├── gerador_csv.py
├── imoveis.py
├── interface.py
├── main.py
├── orcamento.py
├── utilitarios.py
├── visualizacao.py
└── README.md
```
