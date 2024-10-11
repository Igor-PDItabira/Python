genero = input("Informe seu gênero: M - Masculino / F - Feminino ")
idade = int(input("Digite sua idade: "))
tempo = int(input("Digite seu tempo de serviço: "))

a = (genero == "M" and idade >= 65) or (genero == "F" and idade >= 60)
b = tempo > 30
c = idade >= 60 and tempo >= 25

aposentadoria = a or b or c

print(f"Você está apto a aposentar? {aposentadoria}")
