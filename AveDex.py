def pausar():
    input("\nPressione ENTER para voltar ao menu...")


def exibir_menu():
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Ver detalhes de uma ave")
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
    }
]

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()
    opcao_menu = input("Escolha uma opção: ").strip()

    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        listar_aves(catalogo_aves)
    elif opcao_menu == "3":
        print("A AveDex é um catálogo interativo de aves.")
        print("Aos poucos, vamos adicionar busca, comparação, documentação e testes.")

    elif opcao_menu == "0":
        print("Encerrando a AveDex. Até logo!")

    else:
        print("Opção inválida. Digite apenas 0, 1, 2 ou 3.")

    if opcao_menu != "0":
        pausar()
nomes_aves = ["Bem-te-vi", "Canário-da-terra", "João-de-barro"]
for nome_ave in nomes_aves:
    print(nome_ave)

ave = {
    "codigo": "1",
    "nome_popular": "Bem-te-vi",
    "nome_cientifico": "Pitangus sulphuratus",
    "habitat": "Áreas abertas e cidades",
    "alimentacao": "Insetos, frutos e pequenos animais",
    "curiosidade": "Seu canto lembra a expressão bem-te-vi."
}
print(ave["nome_popular"])
catalogo_aves = [
    {"codigo": "1", "nome_popular": "Bem-te-vi"},
    {"codigo": "2", "nome_popular": "Canário-da-terra"}
]
for ave in catalogo_aves:
    print(f"{ave['codigo']} - {ave['nome_popular']}")

def exibir_mensagem_boas_vindas(nome_usuario):
    print(f"Olá, {nome_usuario}!")
    print("Seja bem-vindo(a) à AveDex.")

def exibir_linha():
    print("=" * 40)
def exibir_menu():
    print()
    exibir_linha()
    print("MENU PRINCIPAL")
    exibir_linha()
    print("1 - Ver mensagem de boas-vindas")
    print("2 - Listar aves")
    print("3 - Ver uma curiosidade sobre aves")
    print("4 - Sobre a AveDex")
    print("0 - Sair")
def mostrar_boas_vindas(nome_usuario):
    print(f"Olá, {nome_usuario}!")
    print("Seja bem-vindo(a) à AveDex.")
    print("Aqui vamos conhecer aves e praticar boas práticas.")
def mostrar_ave_inicial():
    print("Ave escolhida: Bem-te-vi")
    print("Nome científico: Pitangus sulphuratus")
    print("O bem-te-vi é uma das aves mais conhecidas do Brasil.")
def mostrar_curiosidade():
    print("Curiosidade:")
    print("Muitas aves ajudam no equilíbrio ambiental ao dispersar sementes.")
def mostrar_sobre():
    print("Sobre a AveDex:")
    print("A AveDex será um catálogo interativo de aves.")
def pausar():
    input("\nPressione ENTER para voltar ao menu...")

if opcao_menu == "1":
    mostrar_boas_vindas(nome_usuario)
elif opcao_menu == "2":
    def listar_aves(catalogo):
        print()
        exibir_linha()
        print("AVES CADASTRADAS")
        exibir_linha()
    for ave in catalogo:
        print(f"{ave['codigo']} - {ave['nome_popular']}")
elif opcao_menu == "3":
    mostrar_curiosidade()
elif opcao_menu == "4":
    mostrar_sobre() 