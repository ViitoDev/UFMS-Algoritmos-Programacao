linhas = int(input('Digite a quantidade de linhas da matriz: '))
colunas = int(input('Digite a quantidade de colunas da matriz: '))

matriz = []
quantidade_pares = 0
quantidade_impares = 0

for i in range(linhas):
	linha = []
	for j in range(colunas):
		valor = int(input(f'Digite o valor da posição [{i}][{j}]: '))
		linha.append(valor)

		if valor % 2 == 0:
			quantidade_pares += 1
		else:
			quantidade_impares += 1
	matriz.append(linha)

print(f'Quantidade de valores pares: {quantidade_pares}')
print(f'Quantidade de valores ímpares: {quantidade_impares}')