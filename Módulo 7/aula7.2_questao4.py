def validador_senha(senha):
    if len(senha) < 8:
        return False

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_caracter_especial = False

    caracteres_especiais = ["@", "#", "$", "%", "^", "&", "*",
                            "(", ")", "-", "_", "+", "=", "<", ">", "?", "/", "~", "`", "|", "{", "}", "[", "]", ":", ";", ".", ",", "!"]

    for char in senha:
        if 'A' <= char <= 'Z':
            tem_maiuscula = True
        elif 'a' <= char <= 'z':
            tem_minuscula = True
        elif '0' <= char <= '9':
            tem_numero = True
        elif char in caracteres_especiais:
            tem_caracter_especial = True

    if tem_maiuscula and tem_minuscula and tem_numero and tem_caracter_especial:
        return True
    else:
        return False


senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))
