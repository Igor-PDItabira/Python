frase = input("Digite uma frase: ")

contagem_vogais = 0
indices_vogais = []

for i, char in enumerate(frase):
    if char.lower() in "aeiou":  # Verifica se o caractere é uma vogal
        contagem_vogais += 1
        indices_vogais.append(i)  # Adiciona o índice da vogal

print(f"Total de vogais: {contagem_vogais}")
print(f"Índices das vogais: {indices_vogais}")
