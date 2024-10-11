classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

aceito = (classe == "guerreiro" and forca > 14 and magia < 11) or (classe == "mago" and forca <
                                                                   11 and magia > 15) or (classe == "arqueiro" and forca > 5 and magia > 5 and forca < 16 and magia < 16)

print(f"Pontos de atributo consistentes com a classe escolhida:  {aceito}")
