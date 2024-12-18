import csv  # Importando a biblioteca CSV para manipular arquivos CSV
import os  # Para limpar a tela


def login():
    # Exibe uma mensagem de boas-vindas e solicita o nome de usuário e senha
    print("\nBem-vindo ao sistema de gerenciamento!")
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    # Lê os usuários do arquivo para validar o login
    usuarios = listar_usuarios()  # Chama a função que retorna a lista de usuários
    for usuario in usuarios:
        # Faz o teste de sistema de login
        if usuario['nome'] == nome and usuario['senha'] == senha:
            if os.name == 'nt':  # Se for Windows
                os.system('cls')
            else:  # Para sistemas Unix/Linux/Mac
                os.system('clear')
            # Funções de Login do sistema
            print(f"Bem-vindo, {nome}!")  # Exibe uma mensagem de sucesso
            return usuario  # Retorna os dados do usuário logado
    print("Usuário ou senha incorretos.")  # Caso não encontre o usuário
    return None  # Retorna None caso o login falhe

# ***USUÁRIO***
# Função para ler o arquivo dos usuários no arquivo [R]


def listar_usuarios():
    # Cria uma lista dos usuários
    usuarios = []
    try:
        # Abre o arquivo CSV de usuários no modo leitura
        with open('usuarios.csv', mode='r') as file:
            reader = csv.reader(file)  # Cria o leitor de CSV
            next(reader)  # Ignora a primeira linha que é o cabeçalho
            # Percorre cada linha do arquivo
            for row in reader:
                # Adiciona os dados do usuário em forma de dicionário
                usuarios.append(
                    {'nome': row[0], 'senha': row[1], 'permissao': row[2]})
    except FileNotFoundError:
        # Caso o arquivo não exista exbe mensagem de erro
        print("O arquivo de usuários não foi encontrado.")
    return usuarios  # Retorna a lista de usuários

# Função para criar um novo usuário no arquivo [C]


def adicionar_usuario(nome, senha, permissao):

    with open('usuarios.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Escreve os dados do novo usuário no arquivo
        writer.writerow([nome, senha, permissao])
    # Mensagem de confirmação da adição de usuário
    print(f"Usuário {nome} adicionado com sucesso!")

# Função para atualizar um usuário no arquivo [U]


def atualizar_usuario(nome, nova_senha=None, nova_permissao=None):
    # Chama a função listar_usuarios para carregar os usuários do arquivo
    usuarios = listar_usuarios()
    # Percorre a lista de usuários
    for usuario in usuarios:
        # Se encontrar o usuário pelo nome
        if usuario['nome'] == nome:
            # Se nova senha for fornecida, atualiza a senha
            if nova_senha:
                usuario['senha'] = nova_senha
            # Se nova permissão for fornecida, atualiza a permissão
            if nova_permissao:
                usuario['permissao'] = nova_permissao
            # Reabre o arquivo de usuários no modo de escrita para salvar as alterações
            with open('usuarios.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                # Cabeçalho do arquivo CSV
                writer.writerow(['nome', 'senha', 'permissao'])
                # Escreve todos os usuários (atualizados) de volta no arquivo
                for u in usuarios:
                    writer.writerow([u['nome'], u['senha'], u['permissao']])
            # Confirmação da atualização
            print(f"Usuário {nome} atualizado com sucesso!")
            return
    print(f"Usuário {nome} não encontrado!")  # Se o usuário não for encontrado

# Função para remover um usuário no arquivo [D]


def remover_usuario(nome):
    # Chama a função listar_usuarios para carregar os usuários do arquivo
    usuarios = listar_usuarios()
    # Filtra os usuários removendo aquele que tem o nome fornecido
    usuarios = [usuario for usuario in usuarios if usuario['nome'] != nome]
    # Reabre o arquivo de usuários no modo de escrita para salvar as alterações
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Cabeçalho do arquivo CSV
        writer.writerow(['nome', 'senha', 'permissao'])
        # Escreve os usuários restantes (sem o removido) de volta no arquivo
        for usuario in usuarios:
            writer.writerow(
                [usuario['nome'], usuario['senha'], usuario['permissao']])
    print(f"Usuário {nome} removido com sucesso!")  # Confirmação da remoção


# ***PRODUTO***
# Função para ler o arquivo dos prdoutos no arquivo [R]
def listar_produtos():
    # Cria uma lista para armazenar os dados dos produtos
    produtos = []
    try:
        # Abre o arquivo CSV de produtos no modo leitura
        with open('produtos.csv', mode='r') as file:
            reader = csv.reader(file)  # Cria o leitor de CSV
            next(reader)  # Ignora a primeira linha que é o cabeçalho
            # Percorre cada linha do arquivo
            for row in reader:
                # Adiciona os dados do produto em forma de dicionário
                produtos.append({'nome': row[0], 'preco': float(
                    row[1]), 'quantidade': int(row[2])})
    except FileNotFoundError:
        # Caso o arquivo não exista
        print("O arquivo de produtos não foi encontrado.")
    return produtos  # Retorna a lista de produtos

# Função para criar um novo produto no arquivo [C]


def adicionar_produto(nome, preco, quantidade):
    # Adiciona um novo produto ao arquivo CSV
    with open('produtos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)  # Cria o escritor de CSV
        # Escreve os dados do novo produto no arquivo
        writer.writerow([nome, preco, quantidade])
    print(f"Produto {nome} adicionado com sucesso!")  # Confirmação da adição

# Função para atualizar um produto no arquivo [C]


def atualizar_produto(nome, novo_preco=None, nova_quantidade=None):
    # Chama a função listar_produtos para carregar os produtos do arquivo
    produtos = listar_produtos()
    # Percorre a lista de produtos
    for produto in produtos:
        # Se encontrar o produto pelo nome
        if produto['nome'] == nome:
            # Se novo preço for fornecido, atualiza o preço
            if novo_preco:
                produto['preco'] = novo_preco
            # Se nova quantidade for fornecida, atualiza a quantidade
            if nova_quantidade:
                produto['quantidade'] = nova_quantidade
            # Reabre o arquivo de produtos no modo de escrita para salvar as alterações
            with open('produtos.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                # Cabeçalho do arquivo CSV
                writer.writerow(['nome', 'preco', 'quantidade'])
                # Escreve todos os produtos (atualizados) de volta no arquivo
                for p in produtos:
                    writer.writerow([p['nome'], p['preco'], p['quantidade']])
            # Confirmação da atualização
            print(f"Produto {nome} atualizado com sucesso!")
            return
    print(f"Produto {nome} não encontrado!")  # Se o produto não for encontrado

# Função para apagar um produto no arquivo [D]


def remover_produto(nome):
    # Chama a função listar_produtos para carregar os produtos do arquivo
    produtos = listar_produtos()
    # Filtra os produtos removendo aquele que tem o nome fornecido
    produtos = [produto for produto in produtos if produto['nome'] != nome]
    # Reabre o arquivo de produtos no modo de escrita para salvar as alterações
    with open('produtos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Cabeçalho do arquivo CSV
        writer.writerow(['nome', 'preco', 'quantidade'])
        # Escreve os produtos restantes (sem o removido) de volta no arquivo
        for produto in produtos:
            writer.writerow(
                [produto['nome'], produto['preco'], produto['quantidade']])
    print(f"Produto {nome} removido com sucesso!")  # Confirmação da remoção

# Função EXtra:
# Ordenação - Por preço


def listar_produtos_por_preco():
    # Chama a função listar_produtos para carregar os produtos
    produtos = listar_produtos()
    # Ordena a lista de produtos pelo preço
    produtos.sort(key=lambda x: x['preco'])
    return produtos  # Retorna a lista de produtos ordenados por preço

# Ordenação - Por nome


def listar_produtos_por_nome():
    # Chama a função listar_produtos para carregar os produtos
    produtos = listar_produtos()
    # Ordena a lista de produtos pelo nome
    produtos.sort(key=lambda x: x['nome'])
    return produtos  # Retorna a lista de produtos ordenados por nome

# Tela de Opções


def exibir_menu(usuario):
    # Exibe o menu com as opções de acordo com a permissão do usuário
    while True:
        if usuario['permissao'] == 'geral':
            print("\nMenu Geral:")
            print("1. Gerenciar Usuários")
            print("2. Gerenciar Produtos")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                menu_usuarios()  # Chama o menu de gerenciamento de usuários
            elif opcao == '2':
                menu_produtos()  # Chama o menu de gerenciamento de produtos
            elif opcao == '3':
                if os.name == 'nt':  # Se for Windows
                    os.system('cls')
                else:  # Para sistemas Unix/Linux/Mac
                    os.system('clear')
                print("Obrigado por usar o nosso sistema!")
                break  # Sai do sistema
            else:
                print("Opção inválida!")

        elif usuario['permissao'] == 'limitado':
            print("\nMenu Limitado:")
            print("1. Gerenciar Produtos")
            print("2. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                menu_produtos()  # Chama o menu de gerenciamento de produtos
            elif opcao == '2':
                if os.name == 'nt':  # Se for Windows
                    os.system('cls')
                else:  # Para sistemas Unix/Linux/Mac
                    os.system('clear')
                print("Obrigado por usar o nosso sistema!")
                break  # Sai do sistema
            else:
                print("Opção inválida!")

# Funções de Menu - Usuário


def menu_usuarios():
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')
    print("\nMenu de Gerenciamento de Usuários:")
    print("1. Adicionar Usuário")
    print("2. Atualizar Usuário")
    print("3. Remover Usuário")
    print("4. Voltar")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do usuário: ")
        senha = input("Senha do usuário: ")
        permissao = input("Permissão do usuário (geral/limitado): ")
        adicionar_usuario(nome, senha, permissao)
    elif opcao == '2':
        nome = input("Nome do usuário a ser atualizado: ")
        nova_senha = input("Nova senha (deixe em branco para não alterar): ")
        nova_permissao = input(
            "Nova permissão (deixe em branco para não alterar): ")
        atualizar_usuario(nome, nova_senha, nova_permissao)
    elif opcao == '3':
        nome = input("Nome do usuário a ser removido: ")
        remover_usuario(nome)
    elif opcao == '4':
        return  # Volta ao menu anterior
    else:
        print("Opção inválida!")

# Funções de Menu - Produtos


def menu_produtos():
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')
    print("\nMenu de Gerenciamento de Produtos:")
    print("1. Adicionar Produto")
    print("2. Atualizar Produto")
    print("3. Remover Produto")
    print("4. Listar Produtos por Nome")
    print("5. Listar Produtos por Preço")
    print("6. Voltar")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: "))
        quantidade = int(input("Quantidade do produto: "))
        adicionar_produto(nome, preco, quantidade)
    elif opcao == '2':
        nome = input("Nome do produto a ser atualizado: ")
        novo_preco = input("Novo preço (deixe em branco para não alterar): ")
        nova_quantidade = input(
            "Nova quantidade (deixe em branco para não alterar): ")
        atualizar_produto(nome, novo_preco if novo_preco else None,
                          nova_quantidade if nova_quantidade else None)
    elif opcao == '3':
        nome = input("Nome do produto a ser removido: ")
        remover_produto(nome)
    elif opcao == '4':
        produtos = listar_produtos_por_nome()
        for p in produtos:
            print(p)
    elif opcao == '5':
        produtos = listar_produtos_por_preco()
        for p in produtos:
            print(p)
    elif opcao == '6':
        return  # Volta ao menu anterior
    else:
        print("Opção inválida!")


# Função Principal
if __name__ == '__main__':
    usuario_logado = login()  # Chama a função de login
    if usuario_logado:
        # Exibe o menu de acordo com o usuário logado
        exibir_menu(usuario_logado)
