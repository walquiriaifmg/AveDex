import unicodedata


# Função que pausa o programa até o usuário pressionar ENTER.
def pausar():
    input("\nPressione ENTER para voltar ao menu...")


def normalizar_texto(texto):
    # Garante que o valor recebido será tratado como texto.
    texto = str(texto)

    # Converte para minúsculas e remove espaços.
    texto = texto.lower().strip()

    # Separa as letras dos sinais de acentuação.
    texto = unicodedata.normalize("NFD", texto)

    # Remove os sinais de acentuação.
    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


# Exibe o menu principal.
def exibir_menu():
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)

    # Exibe as opções disponíveis.
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Comparar duas aves")
    print("5 - Sobre a AveDex")
    print("0 - Sair")


# Lista todas as aves cadastradas.
def listar_aves(catalogo):
    print()
    print("=" * 50)
    print("AVES CADASTRADAS")
    print("=" * 50)

    # Percorre todas as aves do catálogo.
    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


# Procura uma ave pelo ID.
def buscar_ave_por_id(catalogo, id_procurado):
    # Percorre todas as aves do catálogo.
    for ave in catalogo:

        # Compara o ID da ave com o ID informado.
        if str(ave["id"]) == id_procurado:
            return ave

    # Retorna None caso não encontre a ave.
    return None


# Busca aves pelo nome, família, ordem ou dieta.
def buscar_aves(catalogo, termo_busca):
    # Lista que armazenará os resultados.
    resultados = []

    # Normaliza o termo digitado pelo usuário.
    termo = normalizar_texto(termo_busca)

    # Percorre todas as aves cadastradas.
    for ave in catalogo:

        # Campos utilizados na pesquisa.
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        # Junta os campos em um único texto.
        texto_busca = " ".join(campos_busca)

        # Normaliza o texto da ave.
        texto_busca = normalizar_texto(texto_busca)

        # Verifica se o termo aparece no texto.
        if termo in texto_busca:
            resultados.append(ave)

    return resultados


# Exibe os resultados encontrados na busca.
def exibir_resultados_busca(resultados):
    print()
    print("=" * 50)
    print("RESULTADOS DA BUSCA")
    print("=" * 50)

    # Verifica se nenhum resultado foi encontrado.
    if len(resultados) == 0:
        print("Nenhuma ave encontrada.")

    else:
        # Exibe cada ave encontrada.
        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )


# Exibe os detalhes completos de uma ave.
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

    # Caso não exista curiosidade, exibe "Não informada".
    print(
        f"Curiosidade: "
        f"{ave.get('curiosidade', 'Não informada')}"
    )


# Permite selecionar uma ave pelo ID.
def selecionar_ave_por_id(catalogo):
    # Mostra as aves disponíveis.
    listar_aves(catalogo)

    # Solicita o ID ao usuário.
    id_escolhido = input(
        "\nDigite o ID da ave: "
    ).strip()

    # Procura a ave pelo ID.
    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    # Verifica se encontrou a ave.
    if ave_encontrada is None:
        print(
            "Ave não encontrada. "
            "Confira o ID informado."
        )

    else:
        # Exibe os detalhes da ave encontrada.
        exibir_detalhes_ave(ave_encontrada)


# Busca aves pelo nome popular.
def buscar_aves_por_nome(catalogo, termo_busca):
    # Lista que armazenará os resultados.
    resultados = []

    # Percorre todas as aves.
    for ave in catalogo:

        # Converte o nome para letras minúsculas.
        nome = ave["nome_popular"].lower()

        # Converte o termo pesquisado para letras minúsculas.
        termo = termo_busca.lower()

        # Verifica se o termo está no nome da ave.
        if termo in nome:
            resultados.append(ave)

    return resultados


# Tela responsável pela busca de aves.
def tela_busca(catalogo):
    # Solicita o termo da pesquisa.
    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    # Verifica se o usuário não digitou nada.
    if termo == "":
        print(
            "Digite algum texto para realizar a busca."
        )
        return

    # Realiza a busca.
    resultados = buscar_aves(
        catalogo,
        termo
    )

    # Exibe os resultados.
    exibir_resultados_busca(resultados)

    # Se houver resultados, permite visualizar detalhes.
    if len(resultados) > 0:
        escolha = input(
            "\nDigite o ID para ver detalhes "
            "ou ENTER para voltar: "
        ).strip()

        if escolha != "":
            # Procura o ID apenas nos resultados encontrados.
            ave_encontrada = buscar_ave_por_id(
                resultados,
                escolha
            )

            if ave_encontrada is None:
                print(
                    "ID não encontrado nos resultados."
                )

            else:
                exibir_detalhes_ave(
                    ave_encontrada
                )


# Retorna o valor ou "Não informado".
def valor_ou_indisponivel(valor, unidade=""):
    # Verifica se o valor está vazio.
    if valor is None or valor == "":
        return "Não informado"

    # Adiciona a unidade ao valor.
    if unidade != "":
        return f"{valor} {unidade}"

    # Retorna o valor como texto.
    return str(valor)


# Imprime uma linha da tabela de comparação.
def imprimir_linha_comparacao(
    rotulo,
    valor_1,
    valor_2
):
    # Exibe os valores alinhados em colunas.
    print(
        f"{rotulo:<18} | "
        f"{str(valor_1):<25} | "
        f"{str(valor_2):<25}"
    )


# Exibe a comparação entre duas aves.
def exibir_comparacao_aves(ave_1, ave_2):
    # Cabeçalho da comparação.
    print()
    print("=" * 78)
    print("COMPARAÇÃO ENTRE AVES")
    print("=" * 78)

    # Mostra os nomes das aves.
    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )

    print("-" * 78)

    # Comparação do nome científico.
    imprimir_linha_comparacao(
        "Nome científico",
        ave_1.get("nome_cientifico"),
        ave_2.get("nome_cientifico")
    )

    # Comparação da ordem.
    imprimir_linha_comparacao(
        "Ordem",
        ave_1.get("ordem"),
        ave_2.get("ordem")
    )

    # Comparação da família.
    imprimir_linha_comparacao(
        "Família",
        ave_1.get("familia"),
        ave_2.get("familia")
    )

    # Comparação da dieta.
    imprimir_linha_comparacao(
        "Dieta",
        ave_1.get("dieta_tipo"),
        ave_2.get("dieta_tipo")
    )

    # Comparação do habitat.
    imprimir_linha_comparacao(
        "Habitat",
        ave_1.get("habitat"),
        ave_2.get("habitat")
    )

    # Comparação do comprimento.
    imprimir_linha_comparacao(
        "Comprimento",
        valor_ou_indisponivel(
            ave_1.get("comprimento_cm"),
            "cm"
        ),
        valor_ou_indisponivel(
            ave_2.get("comprimento_cm"),
            "cm"
        )
    )

    # Comparação do peso.
    imprimir_linha_comparacao(
        "Peso",
        valor_ou_indisponivel(
            ave_1.get("peso_g"),
            "g"
        ),
        valor_ou_indisponivel(
            ave_2.get("peso_g"),
            "g"
        )
    )

    # Comparação do status de conservação.
    imprimir_linha_comparacao(
        "Conservação",
        ave_1.get(
            "status_conservacao",
            "Não informado"
        ),
        ave_2.get(
            "status_conservacao",
            "Não informado"
        )
    )

    # Comparação do índice de conservação.
    imprimir_linha_comparacao(
        "Índice",
        ave_1.get(
            "indice_conservacao",
            "Não informado"
        ),
        ave_2.get(
            "indice_conservacao",
            "Não informado"
        )
    )


# Permite escolher uma ave pelo ID.
def escolher_ave(catalogo, mensagem):
    # Mostra a lista de aves.
    listar_aves(catalogo)

    # Solicita o ID da ave.
    id_escolhido = input(
        f"\n{mensagem}: "
    ).strip()

    # Procura a ave pelo ID.
    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    # Verifica se encontrou a ave.
    if ave_encontrada is None:
        print(
            "Ave não encontrada. "
            "Confira o ID informado."
        )
        return None

    # Retorna a ave encontrada.
    return ave_encontrada


# Permite comparar duas aves.
def comparar_duas_aves(catalogo):
    print()
    print("Escolha a primeira ave")

    # Escolhe a primeira ave.
    ave_1 = escolher_ave(
        catalogo,
        "Digite o ID da primeira ave"
    )

    # Se a primeira ave não foi encontrada,
    # encerramos a função.
    if ave_1 is None:
        return

    print()
    print("Escolha a segunda ave")

    # Escolhe a segunda ave.
    ave_2 = escolher_ave(
        catalogo,
        "Digite o ID da segunda ave"
    )

    # Se a segunda ave não foi encontrada,
    # encerramos a função.
    if ave_2 is None:
        return

    # Verifica se o usuário escolheu a mesma ave.
    if ave_1["id"] == ave_2["id"]:
        print()
        print(
            "Aviso: você selecionou a mesma ave "
            "nas duas opções."
        )
        print(
            "Escolha duas aves diferentes "
            "para realizar a comparação."
        )
        return

    # Se as aves forem diferentes,
    # exibe a comparação.
    exibir_comparacao_aves(
        ave_1,
        ave_2
    )


# Catálogo de aves.
catalogo_aves = [
    {
        # ID único da ave.
        "id": 1,

        # Nomes da ave.
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",

        # Classificação.
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",

        # Tipo principal de dieta.
        "dieta_tipo": "Onívora",

        # Ambiente onde a ave costuma viver.
        "habitat": (
            "Áreas abertas, cidades "
            "e bordas de florestas"
        ),

        # Medidas aproximadas.
        "comprimento_cm": 23,
        "peso_g": 68,

        # Situação de conservação.
        "status_conservacao": "Pouco preocupante",

        # Índice de conservação.
        "indice_conservacao": 1,

        # Outros detalhes.
        "alimentacao": (
            "Insetos, frutos e pequenos animais"
        ),
        "curiosidade": (
            "Seu canto parece dizer o próprio nome."
        )
    },
    {
        "id": 2,

        "nome_popular": "João-de-barro",
        "nome_cientifico": "Furnarius rufus",

        "ordem": "Passeriformes",
        "familia": "Furnariidae",

        "dieta_tipo": "Insetívora",

        "habitat": (
            "Campos, cidades e áreas rurais"
        ),

        "comprimento_cm": 20,
        "peso_g": 49,

        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,

        "alimentacao": (
            "Insetos e outros invertebrados"
        ),
        "curiosidade": (
            "É conhecido por construir ninhos de barro."
        )
    },
    {
        "id": 3,

        "nome_popular": "Canário-da-terra",
        "nome_cientifico": "Sicalis flaveola",

        "ordem": "Passeriformes",
        "familia": "Thraupidae",

        "dieta_tipo": "Granívora",

        "habitat": "Campos e áreas abertas",

        "comprimento_cm": 13,
        "peso_g": 20,

        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,

        "alimentacao": (
            "Sementes e pequenos insetos"
        ),
        "curiosidade": (
            "Possui canto forte e melodioso."
        )
    }
]


# Variável que armazenará a opção escolhida.
opcao_menu = ""

# Laço principal do programa.
# Continua executando até o usuário escolher 0.
while opcao_menu != "0":

    # Exibe o menu principal.
    exibir_menu()

    # Lê a opção escolhida.
    opcao_menu = input(
        "Escolha uma opção: "
    ).strip()

    if opcao_menu == "1":
        # Lista todas as aves cadastradas.
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        # Abre a tela de busca.
        tela_busca(catalogo_aves)

    elif opcao_menu == "3":
        # Permite visualizar os detalhes de uma ave.
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "4":
        # Permite comparar duas aves.
        comparar_duas_aves(catalogo_aves)

    elif opcao_menu == "5":
        # Exibe informações sobre o projeto.
        print(
            "A AveDex é um catálogo interativo de aves."
        )
        print(
            "Em breve, teremos batalha, imagens, "
            "sons e dados em arquivo JSON."
        )

    elif opcao_menu == "0":
        # Exibe a mensagem de encerramento.
        print(
            "Encerrando a AveDex. Até logo!"
        )

    else:
        # Informa quando uma opção inválida é digitada.
        print(
            "Opção inválida. "
            "Digite apenas 0, 1, 2, 3, 4 ou 5."
        )