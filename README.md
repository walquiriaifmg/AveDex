# AveDex
Catálogo interativo de aves desenvolvido na disciplina de
Boas Práticas de Programação.
## Funcionalidades atuais
- menu em repetição;
- mensagem personalizada;
- apresentação inicial de uma ave;
- tratamento de opção inválida.
## Como executar
```bash
python avedex.py
```
## Fontes dos dados
- Nome da instituição ou site: https://www.wikiaves.com.br/index.php

## Evolução do projeto
Nesta versão, as aves foram organizadas em uma lista de
dicionários e as funcionalidades foram separadas em funções. Além disso foram adicionadas novas aves.

## Testes manuais realizados aula 6
- [x] Listagem das aves
- [x] Consulta de código existente
- [x] Consulta de código inexistente
- [x] Tratamento de opção inválida
- [x] Encerramento do programa

## Testes manuais realizados aula 7
- [x] Listagem de aves
- [x] Seleção de ave por ID existente
- [x] Seleção de ave por ID inexistente
- [x] Opção inválida no menu
- [x] Encerramento do programa

## Testes manuais realizados aula 8
- [x] Busca por parte do nome popular
- [x] Busca ignorando acentos
- [x] Busca por família
- [x] Busca por ordem
- [x] Busca por dieta
- [x] Busca sem resultados
- [x] Busca com entrada vazia
- [x] Tentativa de abrir ID fora dos resultados

## Exemplos de busca aula 8
## Exemplo 1
==================================================
AVEDEX - MENU PRINCIPAL
==================================================
1 - Listar aves
2 - Buscar ave
3 - Ver detalhes de uma ave
4 - Sobre a AveDex
0 - Sair
Escolha uma opção: 2
Digite parte do nome, família, ordem ou dieta: Pica   

==================================================
RESULTADOS DA BUSCA
==================================================
7 - Pica-pau-de-cabeça-amarela (Picidae, Insetívora)

Digite o ID para ver detalhes ou ENTER para voltar: 7

==================================================
DETALHES DA AVE
==================================================
ID: 7
Nome popular: Pica-pau-de-cabeça-amarela
Nome científico: Celeus flavescens
Ordem: Piciformes
Família: Picidae
Dieta: Insetívora
Habitat: Habita florestas tropicais e subtropicais, principalmente em áreas de cerrado e matas secundárias.
Alimentação: Alimenta-se principalmente de insetos, especialmente formigas e cupins, 
que captura perfurando a madeira com seu bico forte e longo.
Curiosidade: É conhecido por seu comportamento territorial e por emitir sons altos e distintivos, que podem ser ouvidos a longas distâncias.

## Exemplo 2
==================================================
AVEDEX - MENU PRINCIPAL
==================================================
1 - Listar aves
2 - Buscar ave
3 - Ver detalhes de uma ave
4 - Sobre a AveDex
0 - Sair
Escolha uma opção: 2
Digite parte do nome, família, ordem ou dieta: aguia

==================================================
RESULTADOS DA BUSCA
==================================================
5 - Águia-solitária (Accipitridae, Carnívora)

Digite o ID para ver detalhes ou ENTER para voltar: 5

==================================================
DETALHES DA AVE
==================================================
ID: 5
Nome popular: Águia-solitária
Nome científico: Urubitinga solitaria
Ordem: Accipitriformes
Família: Accipitridae
Dieta: Carnívora
Habitat: Habita florestas montanhosas úmidas e de pinheiros.
Alimentação: Alimenta-se de lagartos, serpentes e outros pequenos vertebrados.
Curiosidade: Constrói o ninho em uma árvore alta, usando ramos e gravetos, 
geralmente botando apenas um ovo.

## Autor
Wlquiria Mafado
