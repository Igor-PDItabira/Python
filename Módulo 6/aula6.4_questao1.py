pares = [num for num in range(20, 51) if num % 2 == 0]
print("Pares entre 20 e 50:", pares)

quadrados = [x**2 for x in range(1, 10)]
print("Quadrados de 1 a 9:", quadrados)

divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]
print("Números divisíveis por 7 entre 1 e 100:", divisiveis_por_7)

paridade = ['par' if num % 2 == 0 else 'ímpar' for num in range(0, 30, 3)]
print('Paridade dos valores em range(0, 30, 3):', paridade)
