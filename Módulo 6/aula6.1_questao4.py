quantidade1 = int(input("Digite a quantidade de elementos da lista 1: "))
quantidade2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista1 = []
lista2 = []

print(f"Digite os {quantidade1} elementos da lista 1:")
for _ in range(quantidade1):
    elemento = int(input())
    lista1.append(elemento)

print(f"Digite os {quantidade2} elementos da lista 2:")
for _ in range(quantidade2):
    elemento = int(input())
    lista2.append(elemento)

lista_intercalada = []
min_length = min(len(lista1), len(lista2))

for i in range(min_length):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

lista_intercalada.extend(lista1[min_length:])
lista_intercalada.extend(lista2[min_length:])

print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))
