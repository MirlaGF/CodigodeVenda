print("Bem-vindo à companhia logística Mirla Freitas S.A.")

# Função para cadastrar uma peça
def cadastrarPeca(codigo):
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    valor = float(input("Digite o valor da peça: "))

    peca = {
        'Código': codigo,
        'Nome': nome,
        'Fabricante': fabricante,
        'Valor': valor
    }

    return peca

# Função para consultar todas as peças
def consultarTodasPecas(pecas):
    print("\n--- Todas as Peças Cadastradas ---")
    for peca in pecas:
        print("\nCódigo: ", peca['Código'])
        print("Fabricante: ", peca['Fabricante'])
        print("Valor: ", peca['Valor'])

# Função para consultar uma peça por código
def consultarPecaPorCodigo(pecas):
    codigo = input("Digite o código da peça: ")
    for peca in pecas:
        if peca['Código'] == codigo:
            print("\n--- Peça Encontrada ---")
            print("Código: ", peca['Código'])
            print("Nome: ", peca['Nome'])
            print("Fabricante: ", peca['Fabricante'])
            print("Valor: ", peca['Valor'])
            return
    print("\nNenhuma peça encontrada com o código informado.")

# Função para consultar peças por fabricante
def consultarPecaPorFabricante(pecas):
    fabricante = input("Digite o fabricante da peça: ")
    encontradas = False
    for peca in pecas:
        if peca['Fabricante'] == fabricante:
            if not encontradas:
                print("\n--- Peças do Fabricante", fabricante, "---")
                encontradas = True
            print("Código: ", peca['Código'])
            print("Nome: ", peca['Nome'])
            print("Valor: ", peca['Valor'])
    if not encontradas:
        print("\nNenhuma peça encontrada do fabricante informado.")

# Função para remover uma peça
def removerPeca(pecas):
    codigo = input("Digite o código da peça que deseja remover: ")
    for peca in pecas:
        if peca['Código'] == codigo:
            pecas.remove(peca)
            print("\nPeça removida com sucesso.")
            return
    print("\nNenhuma peça encontrada com o código informado.")

# Função principal
def main():
    pecas = []  # Lista para armazenar as peças cadastradas
    contador = 1  # Contador para gerar o código exclusivo das peças

    while True:
        print("\nEscolha a opção desejada:")
        print("1. Cadastrar Peça")
        print("2. Consultar Peça")
        print("3. Remover Peça")
        print("4. Sair")

        opcao = input(">> ")

        if opcao == "1":
            print("Você selecionou a Opção de Cadastrar Peça.")
            codigo_peca = input("Digite o código da peça: ")
            peca = cadastrarPeca(codigo_peca)
            pecas.append(peca)
            print("\nPeça cadastrada com sucesso.")
        
        elif opcao == "2":
            print("Você selecionou a Opção de Consultar Peça.")
            while True:
                print("\n--- Menu de Consulta ---")
                print("1) Consultar Todas as Peças")
                print("2) Consultar Peças por Código")
                print("3) Consultar Peças por Fabricante")
                print("4) Retornar")

                opcao_consulta = input("Digite a opção desejada: ")
                
                if opcao_consulta == "1":
                    consultarTodasPecas(pecas)
                    break
                elif opcao_consulta == "2":
                    consultarPecaPorCodigo(pecas)
                    break
                elif opcao_consulta == "3":
                    consultarPecaPorFabricante(pecas)
                    break
                elif opcao_consulta == "4":
                    break
                else:
                    print("\nOpção inválida. Digite novamente.")
        
        elif opcao == "3":
            print("Você selecionou a Opção de Remover Peça.")
            removerPeca(pecas)
        
        elif opcao == "4":
            print("Saindo do programa...")
            break
        
        else:
            print("\nOpção inválida. Digite novamente.")

# Execução do programa
if __name__ == '__main__':
    main()

# Função para cadastrar uma peça
def cadastrarPeca(codigo):
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    valor = float(input("Digite o valor da peça: "))

    peca = {
        'Código': codigo,
        'Nome': nome,
        'Fabricante': fabricante,
        'Valor': valor
    }

    return peca

# Função para consultar todas as peças
def consultarTodasPecas(pecas):
    print("\n--- Todas as Peças Cadastradas ---")
    for peca in pecas:
        print("\nCódigo: ", peca['Código'])
        print("Fabricante: ", peca['Fabricante'])
        print("Valor: ", peca['Valor'])

# Função para consultar uma peça por código
def consultarPecaPorCodigo(pecas):
    codigo = input("Digite o código da peça: ")
    for peca in pecas:
        if peca['Código'] == codigo:
            print("\n--- Peça Encontrada ---")
            print("Código: ", peca['Código'])
            print("Nome: ", peca['Nome'])
            print("Fabricante: ", peca['Fabricante'])
            print("Valor: ", peca['Valor'])
            return
    print("\nNenhuma peça encontrada com o código informado.")

# Função para consultar peças por fabricante
def consultarPecaPorFabricante(pecas):
    fabricante = input("Digite o fabricante da peça: ")
    encontradas = False
    for peca in pecas:
        if peca['Fabricante'] == fabricante:
            if not encontradas:
                print("\n--- Peças do Fabricante", fabricante, "---")
                encontradas = True
            print("Código: ", peca['Código'])
            print("Nome: ", peca['Nome'])
            print("Valor: ", peca['Valor'])
    if not encontradas:
        print("\nNenhuma peça encontrada do fabricante informado.")

# Função para remover uma peça
def removerPeca(pecas):
    codigo = input("Digite o código da peça que deseja remover: ")
    for peca in pecas:
        if peca['Código'] == codigo:
            pecas.remove(peca)
            print("\nPeça removida com sucesso.")
            return
    print("\nNenhuma peça encontrada com o código informado.")

# Função principal
def main():
    pecas = []  # Lista para armazenar as peças cadastradas
    contador = 1  # Contador para gerar o código exclusivo das peças

    while True:
        print("\nEscolha a opção desejada:")
        print("1. Cadastrar Peça")
        print("2. Consultar Peça")
        print("3. Remover Peça")
        print("4. Sair")

        opcao = input(">> ")

        if opcao == "1":
            print("Você selecionou a Opção de Cadastrar Peça.")
            codigo_peca = input("Digite o código da peça: ")
            peca = cadastrarPeca(codigo_peca)
            pecas.append(peca)
            print("\nPeça cadastrada com sucesso.")
        
        elif opcao == "2":
            print("Você selecionou a Opção de Consultar Peça.")
            while True:
                print("\n--- Menu de Consulta ---")
                print("1) Consultar Todas as Peças")
                print("2) Consultar Peças por Código")
                print("3) Consultar Peças por Fabricante")
                print("4) Retornar")

                opcao_consulta = input("Digite a opção desejada: ")
                
                if opcao_consulta == "1":
                    consultarTodasPecas(pecas)
                    break
                elif opcao_consulta == "2":
                    consultarPecaPorCodigo(pecas)
                    break
                elif opcao_consulta == "3":
                    consultarPecaPorFabricante(pecas)
                    break
                elif opcao_consulta == "4":
                    break
                else:
                    print("\nOpção inválida. Digite novamente.")
        
        elif opcao == "3":
            print("Você selecionou a Opção de Remover Peça.")
            removerPeca(pecas)
        
        elif opcao == "4":
            print("Saindo do programa...")
            break
        
        else:
            print("\nOpção inválida. Digite novamente.")

# Execução do programa
if __name__ == '__main__':
    main()

# Função para cadastrar uma peça
def cadastrarPeca(codigo):
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    valor = float(input("Digite o valor da peça: "))

    peca = {
        'Código': codigo,
        'Nome': nome,
        'Fabricante': fabricante,
        'Valor': valor
    }

    return peca

# Função para consultar todas as peças
def consultarTodasPecas(pecas):
    print("\n--- Todas as Peças Cadastradas ---")
    for peca in pecas:
        print("\nCódigo: ", peca['Código'])
        print("Fabricante: ", peca['Fabricante'])
        print("Valor: ", peca['Valor'])

# Função para consultar uma peça por código
def consultarPecaPorCodigo(pecas):
    codigo = input("Digite o código da peça: ")
    for peca in pecas:
        if peca['Código'] == codigo:
            print("\n--- Peça Encontrada ---")
            print("Código: ", peca['Código'])
            print("Nome: ", peca['Nome'])
            print("Fabricante: ", peca['Fabricante'])
            print("Valor: ", peca['Valor'])
            return
    print("\nNenhuma peça encontrada com o código informado.")

# Função para consultar peças por fabricante
def consultarPecaPorFabricante(pecas):
    fabricante = input("Digite o fabricante da peça: ")
    encontradas = False
    for peca in pecas:
        if peca['Fabricante'] == fabricante:
            if not encontradas:
                print("\n--- Peças do Fabricante", fabricante, "---")
                encontradas = True
            print("Código: ", peca['Código'])
            print("Nome: ", peca['Nome'])
            print("Valor: ", peca['Valor'])
    if not encontradas:
        print("\nNenhuma peça encontrada do fabricante informado.")

# Função para remover uma peça
def removerPeca(pecas):
    codigo = input("Digite o código da peça que deseja remover: ")
    for peca in pecas:
        if peca['Código'] == codigo:
            pecas.remove(peca)
            print("\nPeça removida com sucesso.")
            return
    print("\nNenhuma peça encontrada com o código informado.")

# Função principal
def main():
    pecas = []  # Lista para armazenar as peças cadastradas
    contador = 1  # Contador para gerar o código exclusivo das peças

    while True:
        print("\nEscolha a opção desejada:")
        print("1. Cadastrar Peça")
        print("2. Consultar Peça")
        print("3. Remover Peça")
        print("4. Sair")

        opcao = input(">> ")

        if opcao == "1":
            print("Você selecionou a Opção de Cadastrar Peça.")
            codigo_peca = input("Digite o código da peça: ")
            peca = cadastrarPeca(codigo_peca)
            pecas.append(peca)
            print("\nPeça cadastrada com sucesso.")
        
        elif opcao == "2":
            print("Você selecionou a Opção de Consultar Peça.")
            while True:
                print("\n--- Menu de Consulta ---")
                print("1) Consultar Todas as Peças")
                print("2) Consultar Peças por Código")
                print("3) Consultar Peças por Fabricante")
                print("4) Retornar")

                opcao_consulta = input("Digite a opção desejada: ")
                
                if opcao_consulta == "1":
                    consultarTodasPecas(pecas)
                    break
                elif opcao_consulta == "2":
                    consultarPecaPorCodigo(pecas)
                    break
                elif opcao_consulta == "3":
                    consultarPecaPorFabricante(pecas)
                    break
                elif opcao_consulta == "4":
                    break
                else:
                    print("\nOpção inválida. Digite novamente.")
        
        elif opcao == "3":
            print("Você selecionou a Opção de Remover Peça.")
            removerPeca(pecas)
        
        elif opcao == "4":
            print("Saindo do programa...")
            break
        
        else:
            print("\nOpção inválida. Digite novamente.")

# Execução do programa
if __name__ == '__main__':
    main()


