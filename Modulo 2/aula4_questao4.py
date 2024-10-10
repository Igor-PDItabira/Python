valor = int(input("Digite o valor: "))

n_100 = valor // 100
valor = valor % 100

n_50 = valor // 50
valor = valor % 50

n_20 = valor // 20
valor = valor % 20

n_10 = valor // 10
valor = valor % 10

n_5 = valor // 5
valor = valor % 5

n_2 = valor // 2
valor = valor % 2

n_1 = valor // 1
valor = valor % 1

print(f"{n_100} nota(s) de 100")
print(f"{n_50} nota(s) de 50")
print(f"{n_20} nota(s) de 20")
print(f"{n_10} nota(s) de 10")
print(f"{n_5} nota(s) de 5")
print(f"{n_2} nota(s) de 2")
print(f"{n_1} nota(s) de 1")
