print("Programa de calculo de frete!")
km = int(input("Digite a distância do endereço de entrega: (em Km) "))
quilo = int(input("Digite o peso do produto para entrega: (em quilograma) "))

if (km < 100):
    preco = km * quilo
elif (km <= 300):
    preco = (km * quilo) * 1.5
else:
    preco = (km * quilo) * 2

if (quilo > 10):
    preco = preco + 10

print(f"O valor do frete é R${preco:,.2f}")
