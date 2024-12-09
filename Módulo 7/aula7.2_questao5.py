import random


def embaralhar_palavras(frase):
    palavras = frase.split()
    palavras_embaralhadas = []

    for palavra in palavras:
        if len(palavra) > 2:
            primeiro = palavra[0]
            ultimo = palavra[-1]
            internos = list(palavra[1:-1])
            random.shuffle(internos)
            palavra_embaralhada = primeiro + ''.join(internos) + ultimo
        else:
            palavra_embaralhada = palavra

        palavras_embaralhadas.append(palavra_embaralhada)

    return ' '.join(palavras_embaralhadas)


frase = input('Digite uma frase para embaralhá-la: ')
resultado = embaralhar_palavras(frase)
print(resultado)
