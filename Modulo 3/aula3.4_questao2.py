filme = int(input("Dê uma nota para o filme assistido: [Escala de 1 a 5] "))

if filme == 5:
    print("Você classificou o filme como 'Excelente!'")
elif filme == 4:
    print("Você classificou o filme como 'Muito Bom!'")
elif filme == 3:
    print("Você classificou o filme como 'Bom!'")
elif filme == 2:
    print("Você classificou o filme como 'Regular.'")
elif filme == 1:
    print("Você classificou o filme como 'Ruim.'")
else:
    print("Opção inválida.")
