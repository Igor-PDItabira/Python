import random
import math

soma = 0
n = int(input("Informe quantos número serão utilizados:  "))

for i in range(n):
    aleatorio = random.randint(1, 100)
    soma = soma + aleatorio

n = math.sqrt(soma)

print(f"O resultado da raiz quadrada dos números é: {n}")
