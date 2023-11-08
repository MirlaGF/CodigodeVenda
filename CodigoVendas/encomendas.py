print("Bem-vindo à companhia logística Mirla Freitas S.A.")

def dimensoesObjeto():
    while True:
        try:
            altura = float(input("Digite a altura do objeto (em cm): "))
            comprimento = float(input("Digite o comprimento do objeto (em cm): "))
            largura = float(input("Digite a largura do objeto (em cm): "))

            volume = altura * comprimento * largura
            print("O volume do objeto é:", volume, "cm³")

            if volume < 1000:
                return 10
            elif volume < 10000:
                return 20
            elif volume < 30000:
                return 30
            elif volume < 100000:
                return 50
            else:
                raise ValueError("Não aceitamos objetos com valores tão grandes.")

        except ValueError as e:
            if str(e) == "Não aceitamos objetos com valores tão grandes.":
                print("Não aceitamos objetos com valores tão grandes")
                print("Entre com as dimensões desejadas novamente")
            else:
                print("Você digitou alguma dimensão com valor não numérico.")
                print("Por favor, entre com as dimensões desejadas novamente")

def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto (em kg): "))

            if peso <= 0.1:
                return 1
            elif peso < 1:
                return 1.5
            elif peso < 10:
                return 2
            elif peso < 30:
                return 3
            else:
                raise ValueError("Não aceitamos objetos tão pesados")
        except ValueError as e:
            if str(e) == "Não aceitamos objetos tão pesados":
                print("Não aceitamos objetos tão pesados")
                print("Entre com o peso desejado novamente")
            else:
                print("Você digitou o peso do objeto com valor não numérico.")
                print("Por favor, entre com o peso desejado novamente.")

def rotaObjeto():
    while True:
        try:
            print("Selecione a rota:")
            rota = input("BR - De Brasília para Rio de Janeiro\n"
                         "BS - De Brasília para São Paulo\n"
                         "RB - De Rio de Janeiro para Brasília\n"
                         "RS - De Rio de Janeiro para São Paulo\n"
                         "SR - De São Paulo para Rio de Janeiro\n"
                         "SB - De São Paulo para Brasília\n")

            if rota in ['RS', 'SR']:
                return 1
            elif rota in ['BS', 'SB']:
                return 1.2
            elif rota in ['BR', 'RB']:
                return 1.5
            else:
                print("Você digitou uma rota que não existe.")
                print("Por favor, entre com a rota desejada novamente.")
        except ValueError as e:
            print(e)

# Exemplo de utilização das funções
try:
    dimensoes = dimensoesObjeto()
    peso = pesoObjeto()
    rota = rotaObjeto()

    total = dimensoes * peso * rota

    resultado = "--- Detalhes do Objeto ---\n"
    resultado += "Dimensões: {:.2f}\n".format(dimensoes)
    resultado += "Peso: {:.2f}\n".format(peso)
    resultado += "Rota: {:.2f}\n".format(rota)
    resultado += "Total a ser pago: R$ {:.2f}".format(total)

    print(resultado)

except ValueError as e:
    print("Ocorreu um erro:", str(e))

