# Módulo 2 — Estruturas de Controle de Fluxo

Este módulo reúne exercícios sobre execução sequencial, atribuição e estruturas de controle de fluxo.

A documentação dos exercícios ficará centralizada neste README. Os códigos-fonte permanecem nos arquivos `.py` correspondentes.

## Exercícios

### Exercício 1 — Análise da saída do programa

#### Enunciado

Determine a saída do programa apresentado na atividade.

#### Código analisado

A solução está em [Exercicio-1.py](Exercicio-1.py).

#### Execução passo a passo

As variáveis começam com os valores:

```text
x = 3.0
y = 4.0
z = 5.0
```

As instruções são executadas sequencialmente:

| Instrução | `x` | `y` | `z` |
| --- | ---: | ---: | ---: |
| Valores iniciais | 3.0 | 4.0 | 5.0 |
| `x = -x` | -3.0 | 4.0 | 5.0 |
| `y = y - 1` | -3.0 | 3.0 | 5.0 |
| `z = z + x` | -3.0 | 3.0 | 2.0 |
| `z = z + x - y` | -3.0 | 3.0 | -4.0 |

#### Saída

```text
x = -3.0 , y = 3.0 , z = -4.0
```

#### Conceitos praticados

- Atribuição de valores a variáveis.
- Alteração do sinal de um número com `-x`.
- Atualização de variáveis usando seus valores anteriores.
- Importância da ordem de execução das instruções.
- Uso da função `print()` para exibir valores.

---

### Exercício 2 — Parágrafo de apresentação

#### Enunciado

Escreva um programa que leia o nome, a idade, a altura, o peso e a nacionalidade do usuário e apresente essas informações em forma de um parágrafo.

#### Funcionamento do código atual

O programa solicita quatro informações:

1. Nome.
2. Idade.
3. Peso.
4. Nacionalidade.

Em seguida, utiliza a função `print()` para juntar os dados em uma frase de apresentação.

#### Exemplo de execução

```text
Digite seu nome: João
Digite sua idade: 20
Digite seu peso: 70
Digite sua nacionalidade: brasileiro

Olá! Meu nome é João , tenho 20 anos, peso 70 kg e sou brasileiro
```

#### Conceitos praticados

- Leitura de dados com `input()`.
- Armazenamento de informações em variáveis.
- Concatenação de valores na saída do programa.
- Formatação de uma frase com dados fornecidos pelo usuário.

#### Implementação

A solução está em [Exercicio-2.py](Exercicio-2.py).

#### Observação

O enunciado também solicita a leitura da altura, mas o código atual não possui uma variável nem uma entrada para essa informação.

---

### Exercício 3 — Perímetro de uma circunferência

#### Enunciado

Faça um programa que calcule e escreva na tela o perímetro de uma circunferência a partir do seu raio.

#### Fórmula

O perímetro, também chamado de comprimento da circunferência, é calculado por:

```text
perímetro = 2 × π × raio
```

O programa utiliza `math.pi` para obter o valor aproximado de π.

#### Funcionamento do código

1. Importa o módulo `math`.
2. Lê o raio informado pelo usuário como um número decimal (`float`).
3. Calcula o perímetro usando `2 * math.pi * raio`.
4. Exibe o resultado na tela.

#### Exemplo de execução

Para um raio de `5`:

```text
Digite o raio do círculo: 5
O perímetro do círculo é: 31.41592653589793
```

#### Conceitos praticados

- Importação de módulos com `import`.
- Uso de constantes matemáticas com `math.pi`.
- Leitura de números decimais com `float()`.
- Aplicação de uma fórmula matemática em um programa.
- Exibição de resultados com `print()`.

#### Implementação

A solução está em [Exercicio-3.py](Exercicio-3.py).

---

### Exercício 4 — Distância entre dois pontos

#### Enunciado

Faça um programa que leia dois pontos no espaço bidimensional e calcule a distância entre esses pontos.

#### Fórmula

Para os pontos `A(x1, y1)` e `B(x2, y2)`, a distância é calculada por:

```text
distância = ((x2 - x1)² + (y2 - y1)²)¹ᐟ²
```

#### Funcionamento do código atual

O programa define diretamente os pontos:

```text
A = (2, 4)
B = (-2, 1)
```

Depois, calcula a distância usando os quadrados das diferenças entre as coordenadas:

```text
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
```

#### Cálculo do exemplo

```text
distância = ((-2 - 2)² + (1 - 4)²)¹ᐟ²
distância = (16 + 9)¹ᐟ²
distância = 25¹ᐟ²
distância = 5
```

#### Saída

```text
A distância entre os pontos A e B é: 5.0
```

#### Conceitos praticados

- Representação de pontos por coordenadas.
- Subtração entre coordenadas.
- Potenciação com o operador `**`.
- Cálculo de raiz quadrada usando potência fracionária.
- Aplicação da fórmula da distância entre dois pontos.

#### Implementação

A solução está em [Exercicio-4.py](Exercicio-4.py).

#### Observação

O enunciado solicita a leitura dos dois pontos, mas o código atual utiliza valores fixos para as coordenadas.

---

### Exercício 5 — Menor quantidade de moedas

#### Enunciado

Dado um valor em centavos, determine a menor quantidade de moedas necessária para representá-lo usando moedas de 1, 5, 10, 25 e 50 centavos, além de moedas de 1 real.

#### Funcionamento do código atual

O programa utiliza uma estratégia gulosa:

1. Lê o valor em centavos.
2. Verifica se é possível usar uma moeda de 1 real.
3. Caso não seja possível, tenta usar uma moeda de 50 centavos.
4. Continua verificando as moedas de 25, 10 e 5 centavos.
5. Usa moedas de 1 centavo para completar o valor restante.
6. Repete o processo até que o valor restante seja zero.

As quantidades de cada moeda são armazenadas em variáveis separadas e exibidas ao final.

#### Exemplo

Para o valor de `290` centavos, o resultado é:

```text
Quantidade de moedas de 1 centavo: 0
Quantidade de moedas de 5 centavos: 1
Quantidade de moedas de 10 centavos: 1
Quantidade de moedas de 25 centavos: 1
Quantidade de moedas de 50 centavos: 1
Quantidade de moedas de 1 real: 2
```

São utilizadas 6 moedas no total.

#### Conceitos praticados

- Estrutura de repetição `while`.
- Estrutura condicional `if/elif/else`.
- Decremento de uma variável até atingir zero.
- Estratégia de escolha das maiores moedas primeiro.
- Contagem e exibição de valores.

#### Forma alternativa

Uma forma mais direta de implementar a mesma lógica é utilizar `//` para calcular a quantidade de moedas e `%` para obter o restante:

```python
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
```

O operador `//` indica quantas moedas cabem no valor restante, enquanto `%` mantém apenas o que ainda falta trocar.

#### Implementação

A solução está em [Exercicio-5.py](Exercicio-5.py).

---

### Próximos exercícios

Novos exercícios serão documentados aqui, cada um em sua própria seção.
