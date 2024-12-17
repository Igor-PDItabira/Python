import random

# Função para ler o arquivo com as palavras para o jogo


def ler_palavras():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
        palavras = arquivo.readlines()
    return [palavra.strip() for palavra in palavras]

# Função para ler os estágios do enforcado


def ler_estagios_enforcado():
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
        estagios = arquivo.read().split("\n\n")
    return estagios

# Função para imprimir o progresso do jogador


def imprime_progresso(palavra, letras_corretas):
    progresso = "".join(
        [letra if letra in letras_corretas else "_" for letra in palavra])
    print("Palavra: " + " ".join(progresso))

# Função para imprimir o enforcado com base no número de erros


def imprime_enforcado(erros, estagios):
    print(estagios[erros])

# Função principal do jogo


def jogar():
    palavras = ler_palavras()
    estagios = ler_estagios_enforcado()

    # Escolher palavra aleatoriamente
    palavra_selecionada = random.choice(palavras).lower()
    letras_corretas = set()  # Letras corretas que o jogador já adivinhou
    letras_erradas = set()  # Letras erradas
    tentativas = 6  # Limite de tentativas

    # Exibir o número de letras na palavra
    print(f"A palavra tem {len(palavra_selecionada)} letras.")

    erros = 0  # Contador de erros

    while erros < tentativas:
        imprime_progresso(palavra_selecionada, letras_corretas)
        letra = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi tentada
        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        # Verifica se a letra está na palavra
        if letra in palavra_selecionada:
            letras_corretas.add(letra)
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            letras_erradas.add(letra)
            erros += 1
            imprime_enforcado(erros, estagios)
            print(f"A letra '{letra}' não está na palavra.")

        # Verifica se o jogador adivinhou a palavra
        if all(letra in letras_corretas for letra in palavra_selecionada):
            print(f"Parabéns! Você adivinhou a palavra: {palavra_selecionada}")
            break

    # Se o jogador perdeu
    if erros == tentativas:
        print(f"Você perdeu! A palavra era: {palavra_selecionada}")


if __name__ == "__main__":
    jogar()
