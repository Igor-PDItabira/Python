meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

dia, mes, ano = nascimento.split("/")
mes_extenso = meses[int(mes) - 1]

print(f"Você nasceu no dia {dia} de {mes_extenso} de {ano}.")
