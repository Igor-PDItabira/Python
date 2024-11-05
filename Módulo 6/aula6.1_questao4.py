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
tamanho_list1 = len(lista1)
tamanho_list2 = len(lista2)

if lista1 >= lista2:
    tamanho = len(lista1)
else:
    tamanho = len(lista2)

for i in range(tamanho):
    if i < len(lista1):
        lista_intercalada.append(lista1[i])
    if i < len(lista2):
        lista_intercalada.append(lista2[i])

print('Lista intercalada: ', lista_intercalada)
