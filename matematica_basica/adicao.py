"""
Função de adição de quantos número forem passados como argumento.

Exemplo:
>>> adicao(1, 2, 3, 4) # 10
"""


def adicao(*numeros):
    soma = 0

    for numero in numeros:

        if isinstance(numero, int):
            soma += numero
        elif isinstance(numero, float):
            soma += numero
        else:
            raise ValueError(f"Valor {numero} não é um número inteiro ou decimal.")

    return soma
