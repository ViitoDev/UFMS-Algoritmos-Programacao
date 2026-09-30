# Módulo 3 — Variáveis compostas: Strings, Vetores e Matrizes

Este módulo reúne exercícios relacionados ao processamento de textos e ao uso de variáveis compostas.

A documentação dos exercícios ficará centralizada neste README. Os códigos-fonte permanecem nos arquivos `.py` correspondentes.

## Exercícios

### Exercício 1 — Contagem de uma letra em uma palavra

#### Enunciado

Leia uma palavra e uma letra informadas pelo usuário e verifique quantas vezes essa letra aparece na palavra.

#### Funcionamento do código

1. Lê uma palavra com `input()`.
2. Lê uma letra com `input()`.
3. Utiliza o método `count()` para contar as ocorrências da letra na palavra.
4. Verifica se a letra está presente com o operador `in`.
5. Exibe uma mensagem informando a quantidade encontrada.

#### Exemplo de execução

```text
Digite uma palavra: banana
Digite uma letra: a
A letra 'a' aparece 3 vezes na palavra 'banana'.
```

#### Conceitos praticados

- Leitura de textos com `input()`.
- Armazenamento de strings em variáveis.
- Contagem de ocorrências com `str.count()`.
- Verificação de pertencimento com o operador `in`.
- Uso de f-string para formatar a saída.

#### Observações

- A comparação diferencia letras maiúsculas de minúsculas. Por exemplo, `A` e `a` são consideradas diferentes.
- Se a letra não aparecer na palavra, o programa não exibe nenhuma mensagem.
- Embora o enunciado peça uma letra, o código não impede que o usuário informe mais de um caractere.

#### Implementação

A solução está em [Exercicio-1.py](Exercicio-1.py).

---

### Exercício 2 — Contagem de caracteres de uma frase

#### Enunciado

Leia uma frase, informe a quantidade de caracteres que ela possui ignorando os espaços em branco e mostre também a frase original digitada pelo usuário.

#### Funcionamento do código atual

1. Lê uma frase com `input()`.
2. Inicializa a posição `p` e o contador de espaços.
3. Percorre a frase com um laço `while` enquanto `p` for menor que o tamanho da frase.
4. Verifica se o caractere da posição atual é um espaço.
5. Incrementa `contador_de_espaco` quando encontra um espaço.
6. Calcula os caracteres sem espaços subtraindo a quantidade de espaços do tamanho total da frase.
7. Exibe a quantidade de espaços, os caracteres sem espaços e a frase original.

#### Exemplo de execução

Para a frase `Olá mundo!`:

```text
Digite uma frase: Olá mundo!
 A frase digitada possui 1 espaços em branco.
 A frase digitada possui 9 caracteres no total.
 A frase original digitada foi: Olá mundo!
```

Embora a mensagem use a expressão "no total", o valor `9` corresponde à quantidade de caracteres sem os espaços. A frase possui 10 caracteres quando o espaço também é considerado.

#### Conceitos praticados

- Leitura de frases com `input()`.
- Percorrimento de strings por índice.
- Estrutura de repetição `while`.
- Comparação de caracteres.
- Contagem de caracteres com `len()`.
- Uso de contadores.
- Exibição da frase original com `print()`.

#### Implementação

A solução está em [Exercicio-2.py](Exercicio-2.py).

#### Observação

O código conta apenas o caractere espaço (`" "`). Tabulações e outros tipos de espaços não são contabilizados como espaços em branco.

---

### Exercício 3 — Palavra invertida em letras maiúsculas

#### Enunciado

Leia uma palavra informada pelo usuário e escreva a palavra invertida, utilizando somente letras maiúsculas.

#### Funcionamento do código

1. Lê uma palavra com `input()`.
2. Inverte a palavra usando o fatiamento `[::-1]`.
3. Converte a palavra invertida para maiúsculas com o método `upper()`.
4. Exibe a palavra original.
5. Exibe a palavra invertida em letras maiúsculas.

#### Exemplo de execução

```text
Digite uma palavra: alfabeto
A palavra digitada foi: alfabeto
A palavra invertida é: OTEBAFLA
```

#### Como funciona o fatiamento

O formato geral do fatiamento é `texto[início:fim:passo]`. O passo `-1` percorre os caracteres do final para o início:

```python
palavra[::-1]
```

Depois, o método `upper()` transforma todas as letras em maiúsculas:

```python
palavra[::-1].upper()
```

#### Conceitos praticados

- Leitura de strings com `input()`.
- Fatiamento de strings.
- Inversão de uma sequência com passo `-1`.
- Conversão de texto para maiúsculas com `upper()`.
- Formatação de saída com f-string.

#### Implementação

A solução está em [Exercicio-3.py](Exercicio-3.py).

---

### Exercício 4 — Data de nascimento por extenso

#### Enunciado

Leia uma data de nascimento no formato `dd/mm/aaaa` e imprima a data com o mês escrito por extenso.

#### Funcionamento do código

1. Lê a data completa como uma string.
2. Extrai o dia usando `data[0:2]`.
3. Extrai o mês usando `data[3:5]`.
4. Extrai o ano usando `data[6:10]`.
5. Converte as três partes para números inteiros.
6. Usa uma sequência de condições `if/elif` para substituir o número do mês pelo seu nome.
7. Exibe a data no formato `dia de mês de ano`.

#### Exemplo de execução

```text
Digite uma data do seu aniversário no formato dd/mm/aaaa: 20/02/1995
A data do seu aniversário é: 20 de Fevereiro de 1995
```

#### Como a data é separada

Para a entrada `20/02/1995`, as posições da string são utilizadas da seguinte forma:

```text
data[0:2]  -> 20 -> dia
data[3:5]  -> 02 -> mês
data[6:10] -> 1995 -> ano
```

#### Conceitos praticados

- Leitura de strings com `input()`.
- Fatiamento de strings por posição.
- Conversão de strings para inteiros com `int()`.
- Estruturas condicionais `if` e `elif`.
- Associação entre números e nomes dos meses.
- Formatação de texto com f-string.

#### Implementação

A solução está em [Exercicio-4.py](Exercicio-4.py).

#### Observações

- O programa espera que a data seja informada exatamente no formato `dd/mm/aaaa`.
- A mensagem exibida pelo código fala em "data do seu aniversário", enquanto o enunciado apresenta a frase "Você nasceu em".
- O código não valida se a data realmente existe, por exemplo, se o dia é válido para o mês informado.

---

### Próximos exercícios

Novos exercícios serão documentados aqui, cada um em sua própria seção.
