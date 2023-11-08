# Identificador pessoal: ProgramadorResponsavelMirlaF
print("Bem Vindo a loja de construção Mirla Freitas!")

# Entrada do valor unitário do produto
valor_unitario = float(input("Digite o valor unitário do produto: "))

# Entrada da quantidade do produto
quantidade = int(input("Digite a quantidade do produto: "))

# Cálculo do valor total sem desconto
total_sem_desconto = valor_unitario * quantidade

# Cálculo do desconto com base na tabela fornecida
if quantidade < 10:
    desconto = 0
elif quantidade < 100:
    desconto = 5
elif quantidade < 1000:
    desconto = 10
else:
    desconto = 15

# Cálculo do valor total após o desconto
valor_desconto = total_sem_desconto * (desconto / 100)
total_com_desconto = total_sem_desconto - valor_desconto

# Saída do valor total sem desconto
print("O valor total sem desconto foi: R$ {:.2f}".format(total_sem_desconto))

# Saída do valor total após o desconto
print("O valor total após o desconto foi: R$ {:.2f}".format(total_com_desconto))

# Exemplo de compra com mais de 10 unidades
exemplo_quantidade = 15
exemplo_total_sem_desconto = valor_unitario * exemplo_quantidade
exemplo_desconto = 5
exemplo_valor_desconto = exemplo_total_sem_desconto * (exemplo_desconto / 100)
exemplo_total_com_desconto = exemplo_total_sem_desconto - exemplo_valor_desconto

# Saída de exemplo de compra com mais de 10 unidades
print("\nExemplo de compra com mais de 10 unidades:")
print("Quantidade: {}".format(exemplo_quantidade))
print("Valor total sem desconto: R$ {:.2f}".format(exemplo_total_sem_desconto))
print("Valor total após o desconto: R$ {:.2f}".format(exemplo_total_com_desconto))

