idade_ju = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

idade_ju = idade_ju > 17
idade_cris = idade_cris > 17

print(idade_ju)
print(idade_cris)

entrar = idade_ju or idade_cris

print(entrar)
