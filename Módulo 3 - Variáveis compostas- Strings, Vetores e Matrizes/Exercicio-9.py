linhas = int(input('Digite a quantidade de linhas da matriz: '))
colunas = int(input('Digite a quantidade de colunas da matriz: '))

matriz = []
maior = None
menor = None

for i in range(linhas):
	linha = []
	for j in range(colunas):
		valor = int(input(f'Digite o valor da posição [{i}][{j}]: '))
		linha.append(valor)

		if maior is None or valor > maior:
			maior = valor
		if menor is None or valor < menor:
			menor = valor
	matriz.append(linha)

print(f'Maior elemento da matriz: {maior}')
print(f'Menor elemento da matriz: {menor}')