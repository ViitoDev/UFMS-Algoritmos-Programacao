palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")
quantidade = palavra.count(letra)

if letra in palavra:
    print(f"A letra '{letra}' aparece {quantidade} vezes na palavra '{palavra}'.")