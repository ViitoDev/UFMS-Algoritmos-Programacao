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

### Próximos exercícios

Novos exercícios serão documentados aqui, cada um em sua própria seção.
