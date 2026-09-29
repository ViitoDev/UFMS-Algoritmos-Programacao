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

### Próximos exercícios

Novos exercícios serão documentados aqui, cada um em sua própria seção.
