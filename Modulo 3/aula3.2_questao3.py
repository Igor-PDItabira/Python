idade = int(input("Digite sua idade: "))
jogos = bool(input("Já jogou pelo menos 3 jogos de tabuleiro? "))
vitorias = int(input("Quantos jogos já venceu? "))

idade = idade > 15 and idade < 19
vitorias = vitorias > 1

entrar = idade and jogos and vitorias


print(f"Apto para ingressar no clube de jogos de tabuleiro: {entrar}")
