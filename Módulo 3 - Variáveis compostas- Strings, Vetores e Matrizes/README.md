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

### Próximos exercícios

Novos exercícios serão documentados aqui, cada um em sua própria seção.
