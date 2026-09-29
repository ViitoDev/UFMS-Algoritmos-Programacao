# Módulo 1 — Introdução a algoritmos e programação

Este módulo reúne os exercícios, problemas e atividades introdutórias da disciplina.

A documentação de todos os exercícios do módulo ficará neste único arquivo, organizada por seção. Os códigos-fonte permanecem nos arquivos `.py` correspondentes.

## Exercícios

### Exercício 1 — Pilha de moedas falsas

#### Problema

Existem 10 pilhas com 10 moedas cada. Uma única pilha contém apenas moedas falsas. As moedas verdadeiras pesam 10 g e as falsas pesam 9 g. O objetivo é descobrir qual pilha é falsa usando o menor número de pesagens.

#### Funcionamento do código atual

O programa solicita o peso de 10 moedas e compara o valor informado com 100 g:

- Se o peso for `100`, exibe que todas as moedas são verdadeiras.
- Para qualquer outro valor, exibe que existe alguma moeda falsa.

As variáveis `moeda` e `moeda_falsa` representam os pesos de 10 g e 9 g, mas não são utilizadas nos cálculos atuais.

#### Algoritmo implementado

```text
ler o peso das 10 moedas

se o peso for igual a 100:
    informar que todas as moedas são verdadeiras
caso contrário:
    informar que existe alguma moeda falsa
```

#### Exemplos

- Entrada `100` → `Todas as moedas são verdadeiras.`
- Entrada `99` → `Existe alguma(s) moeda(s) falsa(s).`

#### Limitação atual

O programa verifica apenas se o peso total corresponde a 10 moedas verdadeiras. Ele ainda não identifica qual das 10 pilhas contém as moedas falsas nem implementa a estratégia de uma única pesagem descrita no problema.

#### Implementação

A solução está em [Exercicio-1.py](Exercicio-1.py).

---

### Próximos exercícios

Novos exercícios serão documentados aqui, cada um em sua própria seção, mantendo a consulta do módulo em um único arquivo.
