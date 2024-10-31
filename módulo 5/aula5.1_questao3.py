import random

sorte = random.randint(1, 10)

while True:

    palpite = int(input("Adivinhe o número entre 1 e 10:  "))
    if palpite > sorte:
        print("Muito alto, tente novamente!")
    elif palpite < sorte:
        print("Muito baixo, tente novamente!")
    else:
        print(f"Correto, o número é {sorte}.")
        break
