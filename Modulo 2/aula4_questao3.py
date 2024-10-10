prod1 = str(input("Digite o nome do produto 1: "))
val1 = float(input("Digite o valor do produto 1: "))
quant1 = int(input("Digite a quantidade do produto 1: "))

prod2 = str(input("Digite o nome do produto 2: "))
val2 = float(input("Digite o valor do produto 2: "))
quant2 = int(input("Digite a quantidade do produto 2: "))

prod3 = str(input("Digite o nome do produto 3: "))
val3 = float(input("Digite o valor do produto 3: "))
quant3 = int(input("Digite a quantidade do produto 3: "))

valor = (val1 * quant1) + (val2 * quant2) + (val3 * quant3)


print(f"Total: R${valor:,.2f}")
