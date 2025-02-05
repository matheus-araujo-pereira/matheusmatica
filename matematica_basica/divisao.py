"""
Função de divisão de quantos números forem passados como argumento.

Exemplo:
>>> divisao(100, 2, 5) # 10.0
"""


def divisao(*numeros):
    if not numeros:
        return 1

    resultado = numeros[0]

    for numero in numeros[1:]:
        if isinstance(numero, int) or isinstance(numero, float):
            if numero == 0:
                raise ValueError("Divisão por zero não é permitida.")
            resultado /= numero
        else:
            raise ValueError(f"Valor {numero} não é um número inteiro ou decimal.")

    return resultado
