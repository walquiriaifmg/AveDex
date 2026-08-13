import unicodedata

#============================================================
# CONSTANTES
#============================================================

# Largura usada em títulos e linhas de separação.
LARGURA_TELA = 78

# Lista com as opções exibidas no menu principal.
OPCOES_MENU = [
    "1 - Listar aves",
    "2 - Buscar ave",
    "3 - Ver detalhes de uma ave",
    "4 - Comparar duas aves",
    "5 - Sobre a AveDex",
    "0 - Sair"
]

# Campos usados na busca textual.
CAMPOS_BUSCA = [
    "nome_popular",
    "nome_cientifico",
    "familia",
    "ordem",
    "dieta_tipo"
]

# Campos exibidos na comparação.
# Cada item possui: rótulo na tela, chave do dicionário e unidade.
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
# FUNÇÕES AUXILIARES
# ======================================================================================

def linha(caractere="=", largura=LARGURA_TELA):
    # Retorna uma linha formada pela repetição de um caractere.
    return caractere * largura


def titulo(texto):
    # Exibe um título padronizado.
    print()
    print(linha("="))
    print(texto)
    print(linha("="))


def mensagem_aviso(texto):
    # Exibe uma mensagem simples de aviso.
    print(f"[AVISO] {texto}")


# Função que pausa o programa até o usuário pressionar ENTER.
def pausar():
    input("\nPressione ENTER para voltar ao menu...")


# Função responsável por normalizar textos.
def normalizar_texto(texto):
    # Garante que o valor recebido será tratado como texto.
    texto = str(texto)

    # Converte o texto para letras minúsculas e remove espaços.
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


# Função que exibe o menu principal.
def exibir_menu():
    print()
    print("=" * 50)
    print("AVEDEX - MENU PRINCIPAL")
    print("=" * 50)
    print("1 - Listar aves")
    print("2 - Buscar ave")
    print("3 - Ver detalhes de uma ave")
    print("4 - Comparar duas aves")
    print("5 - Sobre a AveDex")
    print("0 - Sair")


# Função que lista todas as aves cadastradas.
def listar_aves(catalogo):
    titulo("AVES CADASTRADAS")

    # Percorre todas as aves do catálogo.
    for ave in catalogo:
        print(f"{ave['id']} - {ave['nome_popular']}")


# Função que procura uma ave pelo ID.
def buscar_ave_por_id(catalogo, id_procurado):
    # Percorre todas as aves cadastradas.
    for ave in catalogo:

        # Compara o ID da ave com o ID informado.
        if str(ave["id"]) == id_procurado:
            return ave

    # Retorna None caso nenhuma ave seja encontrada.
    return None


# Função que busca aves por diferentes campos.
def buscar_aves(catalogo, termo_busca):
    # Lista que armazenará os resultados.
    resultados = []

    # Normaliza o termo digitado pelo usuário.
    termo = normalizar_texto(termo_busca)

    # Percorre todas as aves cadastradas.
    for ave in catalogo:

        # Campos utilizados na busca.
        campos_busca = [
            ave.get("nome_popular", ""),
            ave.get("nome_cientifico", ""),
            ave.get("familia", ""),
            ave.get("ordem", ""),
            ave.get("dieta_tipo", "")
        ]

        # Junta os campos em um único texto.
        texto_busca = " ".join(campos_busca)

        # Normaliza o texto para facilitar a busca.
        texto_busca = normalizar_texto(texto_busca)

        # Verifica se o termo está presente no texto.
        if termo in texto_busca:
            resultados.append(ave)

    return resultados


# Função que exibe os resultados encontrados.
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


# Função que exibe os detalhes de uma ave.
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

    # Caso a curiosidade não exista, informa que não foi cadastrada.
    print(
        f"Curiosidade: "
        f"{ave.get('curiosidade', 'Não informada')}"
    )


# Função que permite selecionar uma ave pelo ID.
def selecionar_ave_por_id(catalogo):
    # Mostra a lista de aves disponíveis.
    listar_aves(catalogo)

    # Solicita o ID da ave.
    id_escolhido = input(
        "\nDigite o ID da ave: "
    ).strip()

    # Procura a ave pelo ID.
    ave_encontrada = buscar_ave_por_id(
        catalogo,
        id_escolhido
    )

    # Verifica se a ave foi encontrada.
    if ave_encontrada is None:
        print(
            "Ave não encontrada. "
            "Confira o ID informado."
        )

    else:
        # Exibe os detalhes da ave.
        exibir_detalhes_ave(ave_encontrada)


# Função para buscar aves pelo nome popular.
def buscar_aves_por_nome(catalogo, termo_busca):
    # Lista que armazenará os resultados.
    resultados = []

    # Percorre todas as aves.
    for ave in catalogo:

        # Converte o nome da ave para letras minúsculas.
        nome = ave["nome_popular"].lower()

        # Converte o termo pesquisado para letras minúsculas.
        termo = termo_busca.lower()

        # Verifica se o termo aparece no nome.
        if termo in nome:
            resultados.append(ave)

    return resultados


# Função que controla a tela de busca.
def tela_busca(catalogo):
    # Solicita o termo que será pesquisado.
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

    # Permite visualizar os detalhes de um resultado.
    if len(resultados) > 0:
        escolha = input(
            "\nDigite o ID para ver detalhes "
            "ou ENTER para voltar: "
        ).strip()

        if escolha != "":
            # Procura o ID dentro dos resultados.
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


# Função que retorna o valor ou informa que ele não foi cadastrado.
def valor_ou_indisponivel(valor, unidade=""):
    # Verifica se o valor está vazio.
    if valor is None or valor == "":
        return "Não informado"

    # Adiciona a unidade ao valor.
    if unidade != "":
        return f"{valor} {unidade}"

    # Retorna o valor como texto.
    return str(valor)


# Função que imprime uma linha da tabela de comparação.
def imprimir_linha_comparacao(
    rotulo,
    valor_1,
    valor_2
):
    # O rótulo identifica o campo comparado.
    # Os valores são alinhados para formar uma tabela.
    print(
        f"{rotulo:<18} | "
        f"{str(valor_1):<25} | "
        f"{str(valor_2):<25}"
    )


# Função que exibe a comparação entre duas aves.
def exibir_comparacao_aves(ave_1, ave_2):
    # Cabeçalho da comparação.
    print()
    print("=" * 78)
    print("COMPARAÇÃO ENTRE AVES")
    print("=" * 78)

    # Mostra os nomes das duas aves.
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


# Função que permite escolher uma ave.
def escolher_ave(catalogo, mensagem):
    # Mostra a lista de aves antes de pedir o ID.
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

    # Se nenhuma ave for encontrada, avisa o usuário.
    if ave_encontrada is None:
        print(
            "Ave não encontrada. "
            "Confira o ID informado."
        )
        return None

    # Retorna a ave encontrada.
    return ave_encontrada


# Função que compara duas aves.
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

    # Verifica se o usuário escolheu a mesma ave
    # nas duas opções.
    if ave_1["id"] == ave_2["id"]:
        print()
        print(
            "AVISO: você escolheu a mesma ave duas vezes."
        )
        print(
            "Escolha duas aves diferentes para comparar."
        )
        return

    # Se as aves forem diferentes,
    # exibe a comparação.
    exibir_comparacao_aves(
        ave_1,
        ave_2
    )


# ============================================================
# CATÁLOGO DE AVES
# ============================================================

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
        "habitat": "Áreas abertas, cidades e bordas de florestas",

        # Medidas aproximadas usadas na comparação.
        "comprimento_cm": 23,
        "peso_g": 68,

        # Situação de conservação.
        "status_conservacao": "Pouco preocupante",

        # Índice numérico usado na comparação.
        "indice_conservacao": 1,

        # Outros detalhes.
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


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

# Variável que armazenará a opção escolhida pelo usuário.
opcao_menu = ""

# Laço principal do programa.
# Continua executando até que o usuário escolha a opção 0.
while opcao_menu != "0":

    # Exibe o menu principal.
    exibir_menu()

    # Lê a opção digitada pelo usuário.
    opcao_menu = input(
        "Escolha uma opção: "
    ).strip()

    if opcao_menu == "1":
        # Lista todas as aves cadastradas.
        listar_aves(catalogo_aves)

    elif opcao_menu == "2":
        # Abre a tela de busca de aves.
        tela_busca(catalogo_aves)

    elif opcao_menu == "3":
        # Permite selecionar uma ave pelo ID
        # e visualizar seus detalhes.
        selecionar_ave_por_id(catalogo_aves)

    elif opcao_menu == "4":
        # Permite comparar os dados de duas aves.
        comparar_duas_aves(catalogo_aves)

    elif opcao_menu == "5":
        # Exibe informações sobre o projeto AveDex.
        print(
            "A AveDex é um catálogo interativo de aves."
        )
        print(
            "Em breve, teremos batalha, imagens, sons "
            "e dados em arquivo JSON."
        )

    elif opcao_menu == "0":
        # Exibe a mensagem de encerramento.
        print(
            "Encerrando a AveDex. Até logo!"
        )

    else:
        # Informa ao usuário quando uma opção inválida é digitada.
        print(
            "Opção inválida. "
            "Digite apenas 0, 1, 2, 3, 4 ou 5."
        )