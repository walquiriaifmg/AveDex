# Função que pausa o programa até o usuário pressionar ENTER.
def pausar():
    input("\nPressione ENTER para voltar ao menu...")


# Função responsável por exibir o menu principal.
def exibir_menu():
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Ver detalhes de uma ave")
    print("3 - Sobre a AveDex")
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


# Função responsável por mostrar todas as informações da ave selecionada.
def exibir_detalhes_ave(ave):
    print()
    print("=" * 50)
    print("DETALHES DA AVE")
    print("=" * 50)

    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
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

    # Opção 2: escolher uma ave e visualizar seus detalhes.
    elif opcao_menu == "2":
        selecionar_ave_por_id(catalogo_aves)

    # Opção 3: mostrar informações sobre o sistema.
    elif opcao_menu == "3":
        print("A AveDex é um catálogo interativo de aves.")
        print("Aos poucos, vamos adicionar busca, comparação, documentação e testes.")

    # Opção 0: encerrar o programa.
    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    # Caso o usuário digite uma opção inexistente.
    else:
        print("Opção inválida. Digite apenas 0, 1, 2 ou 3.")

    # Após executar qualquer opção (exceto sair), o programa espera o usuário pressionar ENTER
    # antes de voltar ao menu principal.
    if opcao_menu != "0":
        pausar()