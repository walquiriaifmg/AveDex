import unicodedata


# ======================================================================================
# Constantes
# ======================================================================================

LARGURA_TELA = 78

OPCOES_MENU = [
    "1 - Listar aves",
    "2 - Buscar ave",
    "3 - Ver detalhes de uma ave",
    "4 - Comparar duas aves",
    "5 - Sobre a AveDex",
    "0 - Sair"
]

CAMPOS_BUSCA = [
    "nome_popular",
    "nome_cientifico",
    "familia",
    "ordem",
    "dieta_tipo"
]

CAMPOS_COMPARACAO = [
    ("Nome científico", "nome_cientifico", ""),
    ("Ordem", "ordem", ""),
    ("Família", "familia", ""),
    ("Dieta", "dieta_tipo", ""),
    ("Habitat", "habitat", ""),
    ("Comprimento", "comprimento_cm", "cm"),
    ("Peso", "peso_g", "g"),
    ("Conservação", "status_conservacao", ""),
    ("Índice", "indice_conservacao", "")
]


# ======================================================================================
# Funções auxiliares
# ======================================================================================

def linha(caractere="=", largura=LARGURA_TELA):
    # Retorna uma linha com o caractere repetido.
    return caractere * largura


def titulo(texto):
    # Exibe um título padronizado.
    print()
    print(linha("="))
    print(texto)
    print(linha("="))


def mensagem_aviso(texto):
    # Exibe uma mensagem de aviso.
    print(f"[AVISO] {texto}")


def normalizar_texto(texto):
    # Converte para texto.
    texto = str(texto)

    # Padroniza minúsculas e remove espaços extras.
    texto = texto.lower().strip()

    # Separa letras e acentos.
    texto = unicodedata.normalize("NFD", texto)

    # Remove os sinais de acentuação.
    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def pausar():
    # Pausa a execução para o usuário conseguir ler a tela.
    input("\nPressione ENTER para voltar ao menu...")


def valor_ou_indisponivel(valor, unidade=""):
    # Se não houver valor, retorna uma mensagem clara.
    if valor is None or valor == "":
        return "Não informado"

    # Se houver unidade, acrescenta a unidade ao valor.
    if unidade != "":
        return f"{valor} {unidade}"

    return str(valor)


def cortar_texto(texto, tamanho=25):
    # Trata texto ausente.
    if texto is None:
        return "Não informado"

    texto = str(texto).strip()

    # Se o texto já for pequeno, retorna como está.
    if len(texto) <= tamanho:
        return texto

    # Corta o texto e adiciona reticências.
    return texto[: tamanho - 3] + "..."


# ======================================================================================
# Menu e listagem
# ======================================================================================

def exibir_menu():
    # Exibe o menu principal com base na lista OPCOES_MENU.
    titulo("AVEDEX - MENU PRINCIPAL")

    for opcao in OPCOES_MENU:
        print(opcao)


def listar_aves(catalogo):
    titulo("AVES CADASTRADAS")

    print(f"Total de aves cadastradas: {len(catalogo)}")
    print()

    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


def buscar_ave_por_id(catalogo, id_procurado):
    # Procura uma ave pelo ID.
    for ave in catalogo:
        if str(ave["id"]) == id_procurado:
            return ave

    return None


# ======================================================================================
# Detalhes da ave
# ======================================================================================

def exibir_detalhes_ave(ave):
    # Exibe informações detalhadas de uma ave.
    titulo("DETALHES DA AVE")

    print(f"ID: {ave['id']}")
    print(f"Nome popular: {ave['nome_popular']}")
    print(f"Nome científico: {ave['nome_cientifico']}")
    print(f"Ordem: {ave.get('ordem', 'Não informada')}")
    print(f"Família: {ave.get('familia', 'Não informada')}")
    print(f"Dieta: {ave.get('dieta_tipo', 'Não informada')}")
    print(f"Habitat: {ave['habitat']}")
    print(
        f"Comprimento: "
        f"{valor_ou_indisponivel(ave.get('comprimento_cm'), 'cm')}"
    )
    print(
        f"Peso: "
        f"{valor_ou_indisponivel(ave.get('peso_g'), 'g')}"
    )
    print(
        f"Conservação: "
        f"{ave.get('status_conservacao', 'Não informada')}"
    )
    print(
        f"Índice de conservação: "
        f"{ave.get('indice_conservacao', 'Não informado')}"
    )
    print(f"Alimentação: {ave['alimentacao']}")
    print(
        f"Curiosidade: "
        f"{ave.get('curiosidade', 'Não informada')}"
    )


def selecionar_ave_por_id(catalogo):
    # Permite ao usuário escolher uma ave pelo ID.
    listar_aves(catalogo)

    id_escolhido = input(
        "\nDigite o ID da ave: "
    ).strip()

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        mensagem_aviso(
            "Ave não encontrada. Confira o ID informado."
        )
    else:
        exibir_detalhes_ave(ave_encontrada)


# ======================================================================================
# Busca textual
# ======================================================================================

def criar_texto_busca(ave):
    # Monta o texto que será usado na busca.
    valores = []

    for campo in CAMPOS_BUSCA:
        valores.append(str(ave.get(campo, "")))

    texto = " ".join(valores)

    return normalizar_texto(texto)


def buscar_aves(catalogo, termo_busca):
    # Busca aves cujo texto contenha o termo digitado.
    resultados = []

    termo = normalizar_texto(termo_busca)

    for ave in catalogo:
        texto_busca = criar_texto_busca(ave)

        if termo in texto_busca:
            resultados.append(ave)

    return resultados


def exibir_resultados_busca(resultados):
    # Exibe a lista de resultados da busca.
    titulo("RESULTADOS DA BUSCA")

    if len(resultados) == 0:
        mensagem_aviso("Nenhuma ave encontrada.")
    else:
        for ave in resultados:
            print(
                f"{ave['id']} - {ave['nome_popular']} "
                f"({ave['familia']}, {ave['dieta_tipo']})"
            )


def tela_busca(catalogo):
    # Tela completa de busca textual.
    termo = input(
        "Digite parte do nome, família, ordem ou dieta: "
    ).strip()

    if termo == "":
        mensagem_aviso(
            "Digite algum texto para realizar a busca."
        )
        return

    resultados = buscar_aves(
        catalogo,
        termo
    )

    exibir_resultados_busca(resultados)

    if len(resultados) > 0:
        escolha = input(
            "\nDigite o ID para ver detalhes "
            "ou ENTER para voltar: "
        ).strip()

        if escolha != "":
            ave_encontrada = buscar_ave_por_id(
                resultados,
                escolha
            )

            if ave_encontrada is None:
                mensagem_aviso(
                    "ID não encontrado nos resultados."
                )
            else:
                exibir_detalhes_ave(ave_encontrada)


# ======================================================================================
# Comparação entre aves
# ======================================================================================

def imprimir_linha_comparacao(
    rotulo,
    valor_1,
    valor_2
):
    # Imprime uma linha alinhada com rótulo e dois valores.
    print(
        f"{rotulo:<18} | "
        f"{str(valor_1):<25} | "
        f"{str(valor_2):<25}"
    )


def preparar_valor_comparacao(ave, campo, unidade):
    # Busca o valor original da ave.
    valor = ave.get(campo)

    # Habitat costuma ser longo, então cortamos para preservar a tabela.
    if campo == "habitat":
        return cortar_texto(valor, 25)

    return valor_ou_indisponivel(valor, unidade)


def exibir_comparacao_aves(ave_1, ave_2):
    # Exibe duas aves lado a lado.
    print()
    print(linha("=", 78))
    print("COMPARAÇÃO ENTRE AVES")
    print(linha("=", 78))

    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )

    print(linha("-", 78))

    for rotulo, campo, unidade in CAMPOS_COMPARACAO:
        valor_1 = preparar_valor_comparacao(
            ave_1,
            campo,
            unidade
        )

        valor_2 = preparar_valor_comparacao(
            ave_2,
            campo,
            unidade
        )

        imprimir_linha_comparacao(
            rotulo,
            valor_1,
            valor_2
        )


def escolher_ave(catalogo, mensagem):
    # Lista as aves e pede um ID.
    listar_aves(catalogo)

    id_escolhido = input(
        f"\n{mensagem}: "
    ).strip()

    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    if ave_encontrada is None:
        mensagem_aviso(
            "Ave não encontrada. Confira o ID informado."
        )
        return None

    return ave_encontrada

def comparar_duas_aves(catalogo):
    print()
    print(">>> FUNÇÃO COMPARAR DUAS AVES FOI CHAMADA <<<")

    print()
    print("ESCOLHA A PRIMEIRA AVE")

    ave_1 = escolher_ave(
        catalogo,
        "Digite o ID da primeira ave"
    )

    if ave_1 is None:
        return

    print()
    print("ESCOLHA A SEGUNDA AVE")

    ave_2 = escolher_ave(
        catalogo,
        "Digite o ID da segunda ave"
    )

    if ave_2 is None:
        return

    print()
    print(">>> AS DUAS AVES FORAM SELECIONADAS <<<")

    exibir_comparacao_aves(
        ave_1,
        ave_2
    )

# ======================================================================================
# Dados
# ======================================================================================

catalogo_aves = [
    {
        "id": 1,
        "nome_popular": "Bem-te-vi",
        "nome_cientifico": "Pitangus sulphuratus",
        "ordem": "Passeriformes",
        "familia": "Tyrannidae",
        "dieta_tipo": "Onívora",
        "habitat": "Áreas abertas, cidades e bordas de florestas",
        "comprimento_cm": 23,
        "peso_g": 68,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 20,
        "peso_g": 49,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
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
        "comprimento_cm": 13,
        "peso_g": 20,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Sementes e pequenos insetos",
        "curiosidade": "Possui canto forte e melodioso."
    },

    {
        "id": 4,
        "nome_popular": "Arara-azul",
        "nome_cientifico": "Anodorhynchus hyacinthinus",
        "ordem": "Psittaciformes",
        "familia": "Psittacidae",
        "dieta_tipo": "Frugívora",
        "habitat": "Pantanal, cerrado e áreas de mata",
        "comprimento_cm": 100,
        "peso_g": 1500,
        "status_conservacao": "Vulnerável",
        "indice_conservacao": 3,
        "alimentacao": "Frutos, sementes e castanhas",
        "curiosidade": "É considerada uma das maiores araras do mundo."
    },

    {
        "id": 5,
        "nome_popular": "Tucano-toco",
        "nome_cientifico": "Ramphastos toco",
        "ordem": "Piciformes",
        "familia": "Ramphastidae",
        "dieta_tipo": "Onívora",
        "habitat": "Cerrado, campos e bordas de florestas",
        "comprimento_cm": 56,
        "peso_g": 540,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Frutos, insetos, ovos e pequenos animais",
        "curiosidade": "Possui um grande bico colorido."
    },

    {
        "id": 6,
        "nome_popular": "Sabiá-laranjeira",
        "nome_cientifico": "Turdus rufiventris",
        "ordem": "Passeriformes",
        "familia": "Turdidae",
        "dieta_tipo": "Onívora",
        "habitat": "Florestas, jardins, parques e cidades",
        "comprimento_cm": 25,
        "peso_g": 75,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Frutos, insetos e pequenos invertebrados",
        "curiosidade": "É conhecido pelo canto melodioso."
    },

    {
        "id": 7,
        "nome_popular": "Coruja-buraqueira",
        "nome_cientifico": "Athene cunicularia",
        "ordem": "Strigiformes",
        "familia": "Strigidae",
        "dieta_tipo": "Carnívora",
        "habitat": "Campos, áreas abertas e cidades",
        "comprimento_cm": 23,
        "peso_g": 170,
        "status_conservacao": "Pouco preocupante",
        "indice_conservacao": 1,
        "alimentacao": "Insetos, pequenos roedores e outros animais",
        "curiosidade": "Costuma utilizar tocas no solo como abrigo."
    },

    {
        "id": 8,
        "nome_popular": "Águia-cinzenta",
        "nome_cientifico": "Urubitinga coronata",
        "ordem": "Accipitriformes",
        "familia": "Accipitridae",
        "dieta_tipo": "Carnívora",
        "habitat": "Campos, cerrado e áreas abertas",
        "comprimento_cm": 75,
        "peso_g": 3000,
        "status_conservacao": "Em perigo",
        "indice_conservacao": 4,
        "alimentacao": "Mamíferos, aves, répteis e outros animais",
        "curiosidade": "É uma das maiores aves de rapina do Brasil."
    }
]

# ======================================================================================
# Programa principal
# ======================================================================================

opcao_menu = ""

while opcao_menu != "0":
    exibir_menu()

    opcao_menu = input(
        "Escolha uma opção: "
    ).strip()

    if opcao_menu == "1":
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        tela_busca(catalogo_aves)

    elif opcao_menu == "3":
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "4":
        comparar_duas_aves(catalogo_aves)

    elif opcao_menu == "5":
        print(
            "A AveDex é um catálogo interativo de aves."
        )
        print(
            "Em breve, teremos batalha, imagens, sons "
            "e dados em arquivo JSON."
        )

    elif opcao_menu == "0":
        print(
            "Encerrando a AveDex. Até logo!"
        )

    else:
        mensagem_aviso(
            "Opção inválida. "
            "Digite apenas 0, 1, 2, 3, 4 ou 5."
        )

    if opcao_menu != "0":
        pausar()