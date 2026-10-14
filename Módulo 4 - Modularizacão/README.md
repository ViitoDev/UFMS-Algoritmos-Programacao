# Módulo 4 — Modularização

[⬅ Voltar ao início](../README.md)

Este módulo reúne exercícios sobre **funções em Python**: definição com `def`, parâmetros, a instrução `return` e a diferença entre funções que devolvem um valor e procedimentos que apenas exibem informações.

| Arquivo | Tema |
| --- | --- |
| [Exercicio-1.py](Exercicio-1.py) | `print` × `return` |
| [Exercicio-2.py](Exercicio-2.py) | Função que verifica se um número é par |
| [Exercicio-3.py](Exercicio-3.py) | Função com laço `while` (tentativa de fatorial) |

> [!TIP]
> Os arquivos `Exercicio-*.py` apenas definem funções. Para testá-las, execute em modo interativo, por exemplo: `python3 -i Exercicio-2.py` e depois `misterio_3(4)`.

## Exercícios

### Exercício 1 — `print` × `return`

#### Enunciado

O que as funções `misterio_1` e `misterio_2` fazem?

#### Análise

As duas funções recebem dois valores, `a` e `b`, e calculam `a + b`. A diferença está no que fazem com o resultado:

| Função | O que faz com a soma | Valor devolvido |
| --- | --- | --- |
| `misterio_1(a, b)` | Exibe na tela com `print()` | `None` |
| `misterio_2(a, b)` | Devolve com `return` | A soma |

#### Exemplo no modo interativo

```text
>>> r = misterio_1(2, 3)
5
>>> print(r)
None
>>> misterio_2(2, 3)
5
```

`misterio_1` mostra o resultado, mas ele não pode ser reaproveitado pelo restante do programa. Já o valor retornado por `misterio_2` pode ser armazenado em uma variável, usado em outra expressão ou passado para outra função.

#### Conceitos praticados

- Definição de funções com `def`.
- Passagem de parâmetros.
- Diferença entre exibir um valor (`print`) e devolvê-lo (`return`).
- Retorno implícito de `None` em funções sem `return`.

#### Implementação

A solução está em [Exercicio-1.py](Exercicio-1.py).

---

### Exercício 2 — Verificação de número par

#### Enunciado

O que a função `misterio_3` faz?

#### Análise

A função recebe um número inteiro `n` e usa o operador de resto `%` para verificar se ele é divisível por 2:

- Se `n % 2 == 0`, o número é **par** e a função retorna `True`.
- Caso contrário, o número é **ímpar** e a função retorna `False`.

#### Exemplo no modo interativo

```text
>>> misterio_3(4)
True
>>> misterio_3(7)
False
```

#### Conceitos praticados

- Operador de resto da divisão (`%`).
- Estrutura condicional `if/else`.
- Funções que retornam valores booleanos.

#### Implementação

A solução está em [Exercicio-2.py](Exercicio-2.py).

---

### Exercício 3 — Função com laço de repetição

#### Enunciado

O que a função `misterio_4` faz?

#### Análise

A função segue o padrão de um **cálculo de fatorial**: inicia um acumulador `resultado` com `1` e o multiplica sucessivamente pelos valores de `i` dentro de um laço `while`, devolvendo o produto ao final.

#### Rastreamento

Como o contador começa em `i = -1`, as duas primeiras multiplicações são por `-1` e por `0`. Para `n = 3`:

| Iteração | `i` | `resultado` |
| :-: | ---: | ---: |
| Início | -1 | 1 |
| 1 | -1 | -1 |
| 2 | 0 | 0 |
| 3 | 1 | 0 |
| 4 | 2 | 0 |
| 5 | 3 | 0 |

#### Conceitos praticados

- Estrutura de repetição `while`.
- Uso de acumulador multiplicativo.
- Rastreamento (teste de mesa) de variáveis.

#### Observação

Como o laço passa por `i = 0`, o resultado é sempre `0` para qualquer `n >= 0`. Para que a função calcule de fato o fatorial (`n!`), o contador precisaria começar em `i = 1`.

#### Implementação

A solução está em [Exercicio-3.py](Exercicio-3.py).

