"""
Função de subtração de quantos números forem passados como argumento.

Exemplo:
>>> subtracao(10, 2, 3, 4) # 1
"""


def subtracao(*numeros):
    if not numeros:
        return 0

    resultado = numeros[0]

    for numero in numeros[1:]:
        if isinstance(numero, int) or isinstance(numero, float):
            resultado -= numero
        else:
            raise ValueError(f"Valor {numero} não é um número inteiro ou decimal.")

    return resultado
