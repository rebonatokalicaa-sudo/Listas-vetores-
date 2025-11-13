# TechWave Digital - Sistema de Controle de Estoque

Sistema desenvolvido em Python para o Laboratório Prático da Aula 11.  
O projeto aplica conceitos de listas, manipulação de strings, recursividade e leitura/escrita em arquivos `.txt`.

## Objetivo
Criar um sistema simples em modo console que permita:
- Cadastrar produtos (nome, quantidade e preço);
- Listar produtos cadastrados;
- Buscar produtos pelo nome;
- Calcular o total de itens usando recursividade;
- Gerar um relatório final com resumo do estoque.

## Funcionalidades
1. Cadastrar produto  
2. Listar produtos  
3. Buscar produto (por nome, sem diferenciar maiúsculas e minúsculas)  
4. Calcular total de itens (recursivo)  
5. Gerar relatório (`relatorio.txt`)  
6. Sair do sistema  

## Estrutura de Arquivos
estoque.txt -> Armazena os produtos cadastrados
relatorio.txt -> Relatório gerado automaticamente
main.py -> Código principal do sistema
## Formato do Arquivo de Estoque
Cada produto é salvo em uma linha, separado por vírgulas:
nome,quantidade,preco

makefile
Copiar código
Exemplo:
Mouse,10,50.00
Teclado,5,120.00
Monitor,3,899.90

markdown
Copiar código

## Como Executar
1. Instale o Python 3 em seu computador.  
2. Salve o arquivo como `main.py` na mesma pasta do projeto.  
3. Execute o programa no terminal:
python main.py

csharp
Copiar código
4. Escolha uma opção no menu e siga as instruções.

## Exemplo de Relatório
=== RELATÓRIO DE ESTOQUE TECHWAVE ===

Mouse | QTD: 10 | R$ 50.00
Teclado | QTD: 5 | R$ 120.00
Monitor | QTD: 3 | R$ 899.90

TOTAL DE ITENS: 18
VALOR TOTAL: R$ 4199.70

kotlin
Copiar código

## Conclusão
O sistema demonstra o ciclo completo de um programa lógico:
**Entrada → Processamento → Armazenamento → Saída**,  
utilizando funções, listas, recursividade e manipulação de arquivos texto.
