matriz = []
soma_total = 0

linhas = int(input('Digite a quantidade de linhas da matriz: '))
colunas = int(input('Digite a quantidade de colunas da matriz: '))

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f'Digite o valor para a posição [{i}][{j}]: '))
        linha.append(valor)
        soma_total += valor
    matriz.append(linha)

quantidade_elementos = linhas * colunas
media = soma_total / quantidade_elementos

print(f"A soma total dos valores da matriz é: {soma_total}")
print(f"A média dos valores da matriz é: {media}")