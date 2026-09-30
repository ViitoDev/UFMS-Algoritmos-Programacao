frase = input("Digite uma frase: ")
p = 0
contador_de_espaco = 0

while p < len(frase):
    if frase[p] == " ":
        contador_de_espaco += 1
    p += 1

print(f"A frase digitada possui {contador_de_espaco} espaços em branco.")
print(f"A frase digitada possui {len(frase) - contador_de_espaco} caracteres no total.")
print(f"A frase original digitada foi: {frase}")