import unicodedata # Importa a biblioteca que permite manipular caracteres Unicode, 
#como acentos e sinais diacríticos.

# Função que pausa o programa até o usuário pressionar ENTER.
def pausar():
    input("\nPressione ENTER para voltar ao menu...")

def normalizar_texto(texto):
# Garante que o valor recebido será tratado como texto.
    texto = str(texto)
    # Converte para minúsculas e remove espaços no início e no final.
    texto = texto.lower().strip()
    # Separa as letras dos sinais de acentuação.
    # Exemplo: "á" passa a ser tratado como "a" + acento.
    texto = unicodedata.normalize("NFD", texto)
    # Monta um novo texto removendo os sinais de acentuação.
    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
)
    return texto

# Função responsável por exibir o menu principal.
def exibir_menu():
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Sobre a AveDex")
    print("0 - Sair")


# Função que percorre a lista de aves e exibe apenas o ID e o nome popular de cada uma.
def listar_aves(catalogo):
    print()
    print("=" * 50)
    print("AVES CADASTRADAS")
    print("=" * 50)

    # Percorre todas as aves cadastradas no catálogo.
    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


# Função que procura uma ave pelo ID informado pelo usuário.
def buscar_ave_por_id(catalogo, id_procurado):

    # Percorre todas as aves do catálogo.
    for ave in catalogo:

        # Compara o ID da ave com o ID informado.
        if str(ave["id"]) == id_procurado:
            return ave  # Retorna a ave encontrada.

    # Caso nenhuma ave seja encontrada.
    return None

def buscar_aves(catalogo, termo_busca):
    # Lista que receberá todas as aves encontradas.
    resultados = []

    # Normalizamos o termo digitado uma única vez.
    termo = normalizar_texto(termo_busca)

    # Percorremos todas as aves do catálogo.
    for ave in catalogo:

        # Separamos os campos em que a busca será feita.
        # Usamos get() para evitar erro caso alguma chave esteja ausente.
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        # Juntamos todos os campos em um único texto.
        # Assim, a busca pode procurar em todos eles de uma vez.
        texto_busca = " ".join(campos_busca)

        # Normalizamos o texto completo da ave.
        texto_busca = normalizar_texto(texto_busca)

        # Se o termo digitado estiver no texto da ave,
        # adicionamos essa ave aos resultados.
        if termo in texto_busca:
            resultados.append(ave)

    return resultados

def exibir_resultados_busca(resultados):
    print()
    print("=" * 50)
    print("RESULTADOS DA BUSCA")
    print("=" * 50)

    # Se a lista estiver vazia, nada foi encontrado.
    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")
    else:
        # Se houver resultados, mostramos cada ave encontrada.
        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )

# Função responsável por mostrar todas as informações da ave selecionada.
def exibir_detalhes_ave(ave):
    print()
    print("=" * 50)
    print("DETALHES DA AVE")
    print("=" * 50)

    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave['ordem']}")
    print(f"Família: {ave['familia']}")
    print(f"Dieta: {ave['dieta_tipo']}")
    print(f"Habitat: {ave['habitat']}")
    print(f"Alimentação: {ave['alimentacao']}")


    # Caso a curiosidade não exista, exibe "Não informada".
    print(f"Curiosidade: {ave.get('curiosidade', 'Não informada')}")


# Função que permite ao usuário escolher uma ave pelo ID.
def selecionar_ave_por_id(catalogo):

    # Primeiro exibe todas as aves disponíveis.
    listar_aves(catalogo)

    # Solicita o ID da ave ao usuário.
    id_escolhido = input("\nDigite o ID da ave: ").strip()

    # Procura a ave correspondente.
    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

    # Verifica se a ave foi encontrada.
    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        # Exibe os detalhes da ave encontrada.
        exibir_detalhes_ave(ave_encontrada)        

def buscar_aves_por_nome(catalogo, termo_busca):
# Criamos uma lista vazia para guardar as aves encontradas.
    resultados = []
    # Percorremos cada ave cadastrada no catálogo.
    for ave in catalogo:
    # Convertemos o nome da ave para minúsculas. Isso evita diferença entre "Bem" e "bem".
        nome = ave["nome_popular"].lower()
        # Também convertemos o termo digitado para minúsculas.
        termo = termo_busca.lower()
        # O operador "in" verifica se um texto aparece dentro de outro.
        # Exemplo: "barro" está dentro de "joão-de-barro".
        if termo in nome:
            resultados.append(ave)
    # Ao final, devolvemos a lista de aves encontradas.
    return resultados

def tela_busca(catalogo):
    # Pedimos ao usuário o texto que deseja procurar.
    termo = input("Digite parte do nome, família, ordem ou dieta: ").strip()

    # Se o usuário apenas apertar ENTER, não faz sentido buscar.
    if termo == "":
        print("Digite algum texto para realizar a busca.")
        return

    # Chamamos a função que faz a busca.
    resultados = buscar_aves(catalogo, termo)

    # Exibimos os resultados encontrados.
    exibir_resultados_busca(resultados)

    # Se existir pelo menos um resultado, damos a opção
    # de abrir os detalhes de uma ave encontrada.
    if len(resultados) > 0:
        escolha = input(
            "\nDigite o ID para ver detalhes ou ENTER para voltar: "
        ).strip()

        if escolha != "":
            # Aqui buscamos apenas dentro da lista de resultados.
            # Assim, o usuário só abre uma ave que realmente apareceu na busca.
            ave_encontrada = buscar_ave_por_id(resultados, escolha)

            if ave_encontrada is None:
                print("ID não encontrado nos resultados.")
            else:
                exibir_detalhes_ave(ave_encontrada)

# Lista contendo todas as aves cadastradas. Cada ave é representada por um dicionário.
catalogo_aves = [
    {
        # Identificador único da ave.
        "id": 1,

        # Nome popular da ave.
        "nome_popular": "Bem-te-vi",

        # Nome científico.
        "nome_cientifico": "Pitangus sulphuratus",

        # Classificação taxonômica.
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",

        # Tipo de alimentação.
        "dieta_tipo": "Onívora",

        # Informações adicionais.
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto parece dizer o próprio nome."
    },
    {
        "id": 2,
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "ordem": "Passeriformes",
        "familia": "Furnariidae",
        "dieta_tipo": "Insetívora",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e outros invertebrados",
        "curiosidade": "É conhecido por construir ninhos de barro."
    },
    {
        "id": 3,
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "ordem": "Passeriformes",
        "familia": "Thraupidae",
        "dieta_tipo": "Granívora",
        "habitat": "Campos e áreas abertas",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "Possui canto forte e melodioso."
    },
    {
        "id": 4,
        "nome_popular": "Arara-azul",
        "nome_cientifico": "Anodorhynchus hyacinthinus",
        "ordem": "Psittaciformes",
        "familia": "Psittacidae",
        "dieta_tipo": "Frugívora e granívora",
        "habitat": "Pantanal, Cerrado e áreas de palmeiras",
        "alimentacao": "Especializada em frutos de palmeiras",
        "curiosidade": "Encontra-se ameaçada de extinção devido à destruição de seus hábitats e ao "
        "\ncomércio ilegal."
    },
    { "id": 5,
        "nome_popular": "Águia-solitária",
        "nome_cientifico": "Urubitinga solitaria",
        "ordem": "Accipitriformes",
        "familia": "Accipitridae",
        "dieta_tipo": "Carnívora",
        "habitat": "Habita florestas montanhosas úmidas e de pinheiros.",
        "alimentacao": "Alimenta-se de lagartos, serpentes e outros pequenos vertebrados.",
        "curiosidade": "Constrói o ninho em uma árvore alta, usando ramos e gravetos, "
        "\ngeralmente botando apenas um ovo."
    },
    {"id": 6,
        "nome_popular": "Corujinha-do-mato",
        "nome_cientifico": "Megascops choliba",
        "ordem": "Strigiformes",
        "familia": "Strigidae",
        "dieta_tipo": "Insectívora",
        "habitat": "Habita cidades, parques urbanos e fazendas, e também habita capoeiras e beiras de"
        "matas secas ou úmidas.",
        "alimentacao": "Alimenta-se principalmente de grandes artrópodes, como gafanhotos, aranhas, "
        "\nescorpiões e mariposas, especialmente próximos a postes de iluminação. "
        "\nTambém consome pequenos vertebrados, como camundongos, morcegos, rãs e, ocasionalmente, minhocas.",
        "curiosidade": "Voa sem criar grandes turbulências, formadoras dos ruídos característicos do "
        "\nrufar de asas. Com isso, aproxima-se da presa em silêncio, tendo localizado-a antes pela visão "
        "\nou pela audição apurada."
    }
]

# Variável que armazenará a opção escolhida pelo usuário.
opcao_menu = ""

# Laço principal do programa. Continua executando até que o usuário escolha a opção 0.
while opcao_menu != "0":

    # Exibe o menu principal.
    exibir_menu()

    # Lê a opção digitada pelo usuário.
    opcao_menu = input("Escolha uma opção: ").strip()

    # Opção 1: listar todas as aves.
    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    # Opção 2: buscar uma ave por texto (nome, família, ordem ou dieta).
    elif opcao_menu == "2":
        tela_busca(catalogo_aves)

    # Opção 3: escolher uma ave e visualizar seus detalhes.
    elif opcao_menu == "3":
        selecionar_ave_por_id(catalogo_aves)

    # Opção 4: mostrar informações sobre o sistema.
    elif opcao_menu == "4":
        print("A AveDex é um catálogo interativo de aves.")
        print("Em breve, teremos comparação, imagens, sons e dados em arquivo JSON.")

    # Opção 0: encerrar o programa.
    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")
    
    # Caso o usuário digite uma opção inexistente.
    else:
        print("Opção inválida. Digite apenas 0, 1, 2, 3 ou 4.")

    # Após executar qualquer opção (exceto sair), o programa espera o usuário pressionar ENTER
    # antes de voltar ao menu principal.
    
    if opcao_menu != "0":
        pausar()
        
  
