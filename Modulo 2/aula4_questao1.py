comprimento = int(input("Digite o comprimento: "))
largura = int(input("Digite a largura: "))
preco = float(input("Qual o valor do metro quadrado? "))

area = comprimento * largura
valor = area * preco

print(f"O terreno possui {area}m2 e custa R${valor:,.2f}")
