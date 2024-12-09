def verificar_palindromo(frase):
    frase_limpa = ""

    for char in frase:
        if char.isalnum():
            frase_limpa += char.lower()

    return frase_limpa == frase_limpa[::-1]


while True:

    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == 'fim':
        break

    if verificar_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
