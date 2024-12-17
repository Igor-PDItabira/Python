# Definindo os dados dos livros
livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Pai Rico, Pai Pobre", "Robert Kiyosaki", 1997, 336],
    ["Bruna Surfistinha", "Raquel Pacheco", 2005, 384],
    ["Ensaio Sobre a Cegueira", "José Saramago", 1995, 352],
    ["A Arte da Guerra", "Sun Tzu", "500 a.C.", 144],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],
    ["The Witcher", "Andrzej Sapkowski", 1993, 352],
    ["As Crônicas Saxônicas", "Bernard Cornwell", 1995, 352],
    ["O Dom Supremo", "Rhonda Byrne", 2006, 256]
]

# Abrindo o arquivo para escrita (modo 'w')
with open('meus_livros.csv', 'w', encoding='utf-8') as file:
    # Escrevendo os títulos das colunas na primeira linha
    file.write("Título,Autor,Ano de publicação,Número de páginas\n")

    # Escrevendo os dados dos livros
    for livro in livros:
        file.write(f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n")

# Arquivo fechado automaticamente ao final do 'with'
