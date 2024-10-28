n = int(input("Digite quantos respondentes: "))

cont = n
soma = 0

while (cont > 0):
    idade = int(input("Digite a idade do respondente: "))
    soma = soma + idade
    cont = cont - 1

soma = soma / n
print(f"A média da idade é {soma}")
