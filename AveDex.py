def pausar():
    input("\nPressione ENTER para voltar ao menu...")


def exibir_menu():
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Ver detalhes de uma ave")
    print("3 - Sobre a AveDex")
    print("0 - Sair")


def listar_aves(catalogo):
    print()
    print("=" * 50)
    print("AVES CADASTRADAS")
    print("=" * 50)

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave
    return None


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
    print(f"Curiosidade: {ave.get('curiosidade', 'Não informada')}")


def selecionar_ave_por_id(catalogo):
    listar_aves(catalogo)

    id_escolhido = input("\nDigite o ID da ave: ").strip()

    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
    else:
        exibir_detalhes_ave(ave_encontrada)


catalogo_aves = [
    {
        "id": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "alimentacao": "Insetos, frutos e pequenos animais",
        "curiosidade": "Seu canto parece dizer o próprio nome."
    },
    {
        "id": 2,
        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",
        "habitat": "Campos, cidades e áreas rurais",
        "alimentacao": "Insetos e outros invertebrados",
        "curiosidade": "É conhecido por construir ninhos de barro."
    },
    {
        "id": 3,
        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",
        "habitat": "Campos e áreas abertas",
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "Possui canto forte e melodioso."
    },
    {
        "id": "4",
        "nome_popular": "Tucano-de-bico-preto",
        "nome_cientifico": "Ramphastos vitellinus",
        "habitat": "Comum na copa de florestas úmidas, tanto em seu interior quanto nas bordas, e em capoeiras altas.",
        "alimentacao": "Frutos e artrópodes em geral",
        "curiosidade": "Seu nome científico significa: Ave de cor laranja com nariz grande como uma espada."
    },
    {
        "id": "5",
        "nome_popular": "Águia-solitária",
        "nome_cientifico": "Urubitinga solitaria",
        "habitat": "Habita florestas montanhosas úmidas e de pinheiros.",
        "alimentacao": "Alimenta-se de lagartos, serpentes e outros pequenos vertebrados.",
        "curiosidade": "Constrói o ninho em uma árvore alta, usando ramos e gravetos, geralmente botando apenas um ovo."
    },
    {
        "id": "6",
        "nome_popular": "Pica-pau-de-cabeça-amarela",
        "nome_cientifico": "Celeus flavescens",
        "habitat": "Florestas tropicais e subtropicais, principalmente em áreas de cerrado.",
        "alimentacao": "Insetos, larvas e formigas.",
        "curiosidade": "É conhecido por seu bico forte e por fazer buracos em árvores para se alimentar."
    },
    {
        "id": "7",
        "nome_popular": "Gavião-branco",
        "nome_cientifico": "Pseudastur albicollis",
        "habitat": "Habita florestas densas e cerrado mais arbóreo, geralmente em ambientes próximos a corpos d'água.",
        "alimentacao": "Alimenta-se de invertebrados, lagartos pequenos, pequenos mamíferos e anfibios.",
        "curiosidade": "Normalmente vive solitário. Geralmente é visto voando em círculos no meio da manhã ou pousado no dossel da floresta."
    }
]

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()
    opcao_menu = input("Escolha uma opção: ").strip()

    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "3":
        print("A AveDex é um catálogo interativo de aves.")
        print("Aos poucos, vamos adicionar busca, comparação, documentação e testes.")

    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    else:
        print("Opção inválida. Digite apenas 0, 1, 2 ou 3.")

    if opcao_menu != "0":
        pausar()