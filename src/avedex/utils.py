import unicodedata

LARGURA_TELA = 78

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

def pausar():
    # Pausa o programa para o usuário conseguir ler a tela.
    input("\nPressione ENTER para voltar ao menu...")

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

