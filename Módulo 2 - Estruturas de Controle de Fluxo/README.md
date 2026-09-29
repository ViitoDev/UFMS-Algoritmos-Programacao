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

### Próximos exercícios

Novos exercícios serão documentados aqui, cada um em sua própria seção.
