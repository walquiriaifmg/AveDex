# AveDex
A AveDex é um catálogo interativo de aves desenvolvido na disciplina de
Boas Práticas de Programação.
## Como executar
```bash
python main.py
```
## Estrutura do projeto
- `main.py`: inicia o programa.
- `src/avedex/app.py`: controla o fluxo principal.
- `src/avedex/interface.py`: mostra abertura e menu.
- `src/avedex/dados.py`: carrega o dataset JSON.
- `src/avedex/catalogo.py`: lista, busca e mostra detalhes.
- `src/avedex/comparacao.py`: compara duas aves.
- `src/avedex/creditos.py`: mostra informações e fontes.
- `src/avedex/utils.py`: reúne funções auxiliares.
- `data/avedex_dataset_midias.json`: dados das aves.

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

## Testes manuais realizados aula 9
- [x] Comparação entre duas aves existentes
- [x] Comparação exibindo família, dieta e habitat
- [x] Comparação exibindo peso e comprimento
- [x] Comparação exibindo status e índice de conservação
- [x] Tratamento de ID inexistente na comparação
- [x] Comparação da mesma ave com ela mesma
- [x] Opção inválida no menu

## Testes de regressão aula 10
- [x] Listar aves
- [x] Buscar por parte do nome
- [x] Buscar por família
- [x] Buscar por ordem
- [x] Buscar por dieta
- [x] Ver detalhes por ID
- [x] Comparar duas aves
- [x] Tratar ID inexistente
- [x] Tratar opção inválida no menu
- [x] Encerrar o programa

## Testes manuais realizados na aula 11
- [x] Execução com `python main.py`
- [x] Carregamento das aves pelo JSON
- [x] Listagem das aves
- [x] Busca textual
- [x] Detalhes por ID
- [x] Comparação entre aves
- [x] Créditos e fontes
- [x] Encerramento do programa

## Autor
Wlquiria Mafado
