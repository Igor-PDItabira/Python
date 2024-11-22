frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

# Ordena a palavra objetivo para comparar com as outras palavras
palavra_objetivo_ordenada = ''.join(sorted(palavra_objetivo))

# Divide a frase em palavras
palavras = frase.split()

# Inicializa a lista para armazenar os anagramas
anagramas = []

# Verifica cada palavra na frase
for palavra in palavras:
    # Ordena a palavra e compara com a palavra objetivo ordenada
    if ''.join(sorted(palavra)) == palavra_objetivo_ordenada:
        anagramas.append(palavra)

# Exibe os anagramas encontrados
print("Anagramas:", anagramas)