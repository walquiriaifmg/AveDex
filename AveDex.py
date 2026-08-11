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

def valor_ou_indisponivel(valor, unidade=""):
    # Se o valor for None ou texto vazio, informamos isso ao usuário.
    if valor is None or valor == "":
        return "Não informado"

    # Se uma unidade foi informada, adicionamos essa unidade ao valor.
    # Exemplo: valor 23 com unidade "cm" vira "23 cm".
    if unidade != "":
        return f"{valor} {unidade}"

    # Se não houver unidade, retornamos o valor como texto.
    return str(valor)

def imprimir_linha_comparacao(rotulo, valor_1, valor_2):
    # O rótulo identifica o campo comparado.
    # Exemplo: "Família", "Dieta" ou "Peso".
    #
    # O símbolo :<18 significa:
    # alinhar à esquerda em um espaço de 18 caracteres.
    #
    # Isso ajuda a deixar a saída parecida com uma tabela.

    print(f"{rotulo:<18} | {str(valor_1):<25} | {str(valor_2):<25}")

def exibir_comparacao_aves(ave_1, ave_2):
    # Cabeçalho da comparação.
    print()
    print("=" * 78)
    print("COMPARAÇÃO ENTRE AVES")
    print("=" * 78)

    # Primeira linha: mostra os nomes das duas aves.
    imprimir_linha_comparacao(
        "Campo",
        ave_1["nome_popular"],
        ave_2["nome_popular"]
    )

    print("-" * 78)

    # Linhas de comparação textual.
    imprimir_linha_comparacao(
        "Nome científico",
        ave_1.get("nome_cientifico"),
        ave_2.get("nome_cientifico")
    )

    imprimir_linha_comparacao(
        "Ordem",
        ave_1.get("ordem"),
        ave_2.get("ordem")
    )

    imprimir_linha_comparacao(
        "Família",
        ave_1.get("familia"),
        ave_2.get("familia")
    )

    imprimir_linha_comparacao(
        "Dieta",
        ave_1.get("dieta_tipo"),
        ave_2.get("dieta_tipo")
    )

    imprimir_linha_comparacao(
        "Habitat",
        ave_1.get("habitat"),
        ave_2.get("habitat")
    )

    # Linhas de comparação numérica com unidade.
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

    imprimir_linha_comparacao(
        "Conservação",
        ave_1.get("status_conservacao", "Não informado"),
        ave_2.get("status_conservacao", "Não informado")
    )

    imprimir_linha_comparacao(
        "Índice",
        ave_1.get("indice_conservacao", "Não informado"),
        ave_2.get("indice_conservacao", "Não informado")
    )

def escolher_ave(catalogo, mensagem):
    # Mostra a lista de aves antes de pedir o ID.
    listar_aves(catalogo)

    # A mensagem muda conforme a situação.
    # Exemplo: "Digite o ID da primeira ave".
    id_escolhido = input(f"\n{mensagem}: ").strip()

    # Reaproveitamos a função que já busca ave por ID.
    ave_encontrada = buscar_ave_por_id(catalogo, id_escolhido)

    # Se nenhuma ave for encontrada, avisamos e retornamos None.
    if ave_encontrada is None:
        print("Ave não encontrada. Confira o ID informado.")
        return None

    # Se encontrou, devolvemos a ave escolhida.
    return ave_encontrada

def comparar_duas_aves(catalogo):
    print()
    print("Escolha a primeira ave")

    # Escolhe a primeira ave.
    ave_1 = escolher_ave(
        catalogo,
        "Digite o ID da primeira ave"
    )

    # Se a primeira ave não foi encontrada, encerramos a função.
    if ave_1 is None:
        return

    print()
    print("Escolha a segunda ave")

    # Escolhe a segunda ave.
    ave_2 = escolher_ave(
        catalogo,
        "Digite o ID da segunda ave"
    )

    # Se a segunda ave não foi encontrada, encerramos a função.
    if ave_2 is None:
        return

    # Se as duas aves existem, exibimos a comparação.
    exibir_comparacao_aves(ave_1, ave_2)

    
# Lista contendo todas as aves cadastradas. Cada ave é representada por um dicionário.
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
        # Nesta versão didática, usamos texto simples.
        "status_conservacao": "Pouco preocupante",

        # Índice numérico que será útil futuramente na batalha.
        # Quanto maior, maior será o nível de atenção na conservação.
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
        
 
