# Identificador pessoal: ProgramadorResponsavelMirlaF
print("Bem Vindo a lanchonete da Mirla Freitas!")
# Descrição do cardápio
print("************Cardápio************")
print("| Código |    Descrição                 | Valor|")
print("|   100  |    Cachorro Quente           |  9,00|")
print("|   101  |    Cachorro Quente  duplo    |  11,00|")
print("|   102  |    X-Egg                     |  12,00|")
print("|   103  |    X-Salada                  |  13,00|")
print("|   104  |    X-Bacon                   |  14,00|")
print("|   105  |    X-Tudo                    |  17,00|")
print("|   200  |    Refrigerante Lata         |   5,00|")
print("|   201  |    Chá Gelado                |   4,00|")
# Tabela de produtos
tabela_produtos = {
    100: {'descrição': 'Cachorro-Quente', 'valor': 9.00},
    101: {'descrição': 'Cachorro-Quente Duplo', 'valor': 11.00},
    102: {'descrição': 'X-Egg', 'valor': 12.00},
    103: {'descrição': 'X-Salada', 'valor': 13.00},
    104: {'descrição': 'X-Bacon', 'valor': 14.00},
    105: {'descrição': 'X-Tudo', 'valor': 17.00},
    200: {'descrição': 'Refrigerante Lata', 'valor': 5.00},
    201: {'descrição': 'Chá Gelado', 'valor': 4.00}
}

total_conta = 0.0
    
while True:
        # Entrada do código do produto
    codigo_produto = input("Entre com o código desejado: ")

    if codigo_produto == 'sair':
        break

    if not codigo_produto.isdigit():
        print("Opção inválida.")
        continue

    codigo_produto = int(codigo_produto)

    if codigo_produto not in tabela_produtos:
        print("Opção inválida.")
        continue

    produto = tabela_produtos[codigo_produto]
    total_conta += produto['valor']

    print(f"Você pediu um {produto['descrição']} no valor de R${produto['valor']:.2f} ")

    resposta = input("Deseja pedir mais alguma coisa?\n1 - SIM\n0 - NÃO\n>> ")

    if resposta.lower() == '0':
        break

print(f"\nValor total: R${total_conta:.2f}")
        
