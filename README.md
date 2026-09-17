# TAPRB-2026

Projeto desenvolvido para a atividade de Azure Functions.

## Integrantes

Anderson
Carlos
David
Vitor Morini

## Azure Functions

O projeto possui duas funções:

### HTTP Function

Recebe um parâmetro através de uma requisição GET.

Exemplo:

`/api/receber?nome=Teste`

A função retorna a informação recebida junto com um texto identificando a função.

### Timer Function

Executa automaticamente a cada minuto e realiza uma chamada HTTP para a HTTP Function, enviando uma informação como parâmetro.

## Tecnologias

- Python
- Azure Functions
- Azure Functions Core Tools
- Git
- GitHub