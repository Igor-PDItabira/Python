def calcular_digito_verificador(digitos, multiplicadores):
    soma = sum(int(digitos[i]) * multiplicadores[i]
               for i in range(len(digitos)))
    resto = soma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto


def validar_cpf(cpf):
    cpf = ''.join([char for char in cpf if char.isdigit()])

    if len(cpf) != 11:
        return "Inválido"

    digitos = cpf[:9]
    digito_1 = int(cpf[9])
    digito_2 = int(cpf[10])

    multiplicadores_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    primeiro_digito_calculado = calcular_digito_verificador(
        digitos, multiplicadores_1)

    if primeiro_digito_calculado != digito_1:
        return "Inválido"

    multiplicadores_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    segundo_digito_calculado = calcular_digito_verificador(
        digitos + str(primeiro_digito_calculado), multiplicadores_2)

    if segundo_digito_calculado != digito_2:
        return "Inválido"

    return "Válido"


# Solicitar o CPF ao usuário
cpf = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")

# Chamar a função de validação e imprimir o resultado
print(validar_cpf(cpf))
