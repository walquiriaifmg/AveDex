from src.avedex.utils import (
    titulo,
    mensagem_aviso,
    normalizar_texto,
    valor_ou_indisponivel,
)

CAMPOS_BUSCA = [
    "nome_popular",
    "nome_cientifico",
    "familia",
    "ordem",
    "dieta_tipo"
]

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
