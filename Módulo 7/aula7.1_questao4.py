numero = input("Digite o número: ")

if len(numero) == 8:
    numero = '9' + numero
    numero_formatado = numero[:5] + '-' + numero[5:]
    print(f"Número completo: {numero_formatado}")
elif len(numero) == 9:
    if numero[0] != '9':
        print("Número inválido: O primeiro dígito deve ser 9.")
    else:
        numero_formatado = numero[:5] + '-' + numero[5:]
        print(f"Número completo: {numero_formatado}")
else:
    print("Número inválido: O número deve ter 8 ou 9 dígitos.")
