import re
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_arquivo = os.path.join(diretorio_atual, "estomago.txt")


def contar_personagens(texto):
    nonato_pattern = r'\bNonato\b'
    iria_pattern = r'\bÍria\b'

    nonato_count = len(re.findall(nonato_pattern, texto, flags=re.IGNORECASE))
    iria_count = len(re.findall(iria_pattern, texto, flags=re.IGNORECASE))

    return nonato_count, iria_count


with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print("Primeiras 25 linhas:")
for i in range(min(25, len(linhas))):
    print(linhas[i].strip())

num_linhas = len(linhas)
print(f"\nNúmero de linhas do arquivo: {num_linhas}")

linha_maior = max(linhas, key=len)
print(f"\nA linha com maior número de caracteres tem {
      len(linha_maior)} caracteres.")
print(f"Linha: {linha_maior.strip()}")

texto_completo = "".join(linhas)
nonato_count, iria_count = contar_personagens(texto_completo)

print(f"\nNúmero de menções a 'Nonato': {nonato_count}")
print(f"Numero de menções a 'Íria': {iria_count}")
