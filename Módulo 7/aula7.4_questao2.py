import re
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_frase = os.path.join(diretorio_atual, "frase.txt")
caminho_palavras = os.path.join(diretorio_atual, "palavras.txt")

with open(caminho_frase, "r") as arquivo:
    frase = arquivo.read()

palavras = re.findall(r'[a-zA-Záéíóúãõâêîôûàèìòùç]+', frase)

with open(caminho_palavras, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")


with open(caminho_palavras, "r") as arquivo:
    print(arquivo.read())
