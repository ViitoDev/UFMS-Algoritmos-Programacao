lista = []

for i in range(5):
    valor = int(input(f'Digite o {i+1}º valor: '))
    lista.append(valor)
    print(f"O valor  {valor} foi adicionado à lista na posição {i}.\n")

input_valor = int(input("Digite um valor para verificar se ele está na lista: "))

posicao = -1

for i in range(len(lista)):
    if lista[i] == input_valor:
        posicao = i
        break

print(posicao)