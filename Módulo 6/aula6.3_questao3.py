import random

lista = [random.randint(-10, 10) for _ in range(20)]


def intervalo_com_mais_negativos(lista):
    max_negativos = 0
    intervalo = (0, 0)

    for i in range(len(lista)):
        for j in range(i+1, len(lista)+1):
            # Contar quantos números negativos há no intervalo
            negativos = sum(1 for x in lista[i:j] if x < 0)
            if negativos > max_negativos:
                max_negativos = negativos
                intervalo = (i, j)

    return intervalo


print("Original:", lista)

inicio, fim = intervalo_com_mais_negativos(lista)

del lista[inicio:fim]

print("Editada:", lista)
