valor_soma = 0
matriz = [[1,2],
          [3,4]]

for i in range(len(matriz)):
    valor_soma += sum(matriz[i])

print(f"A soma dos valores da matriz é: {valor_soma}")