from src.avedex.catalogo import escolher_ave
from src.avedex.utils import (
    linha,
    titulo,
    valor_ou_indisponivel,
    cortar_texto,
)

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