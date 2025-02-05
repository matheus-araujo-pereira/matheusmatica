"""
Função de multiplicação de quantos números forem passados como argumento.

Exemplo:
>>> multiplicacao(2, 3, 4) # 24
"""


def multiplicacao(*numeros):
    if not numeros:
        return 1

    resultado = 1

    for numero in numeros:
        if isinstance(numero, int) or isinstance(numero, float):
            resultado *= numero
        else:
            raise ValueError(f"Valor {numero} não é um número inteiro ou decimal.")

    return resultado
