quantidade = int(input("Digite a quantidade de centavos que você deseja trocar: "))

moedas_100 = quantidade // 100
quantidade %= 100

moedas_50 = quantidade // 50
quantidade %= 50

moedas_25 = quantidade // 25
quantidade %= 25

moedas_10 = quantidade // 10
quantidade %= 10

moedas_5 = quantidade // 5
quantidade %= 5

moedas_1 = quantidade

print("Quantidade de moedas de 1 centavo:", moedas_1)
print("Quantidade de moedas de 5 centavos:", moedas_5)
print("Quantidade de moedas de 10 centavos:", moedas_10)
print("Quantidade de moedas de 25 centavos:", moedas_25)
print("Quantidade de moedas de 50 centavos:", moedas_50)
print("Quantidade de moedas de 1 real:", moedas_100)