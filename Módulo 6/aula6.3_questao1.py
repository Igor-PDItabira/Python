numeros = []
print("Digite números inteiros. Para parar, digite 'fim'.")
while True:
    entrada = input("Digite um número: ")
    if entrada == 'fim':
        if len(numeros) < 4:
            print("Você deve inserir pelo menos 4 números.")
        else:
            break
    else:
        numeros.append(entrada)


print("\nLista original:", numeros)

print("Os 3 primeiros elementos:", numeros[:3])

print("Os 2 últimos elementos:", numeros[-2:])

print("Lista invertida:", numeros[::-1])

print("Elementos de índice par:", numeros[::2])

print("Elementos de índice ímpar:", numeros[1::2])
