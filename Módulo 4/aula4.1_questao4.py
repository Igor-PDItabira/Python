n = int(input("Digite quantos números serão testados: "))

maior = 0

while (n > 0):
    x = int(input("Digite um valor: "))

    if (x > maior):
        maior = x
    n = n - 1

print(maior)
