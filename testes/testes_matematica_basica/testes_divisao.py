import unittest
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../matematica_basica")),
)

from divisao import divisao


class TestDivisao(unittest.TestCase):

    def teste_divisao_inteiros(self):
        self.assertEqual(divisao(100, 2, 5), 10.0)

    def teste_divisao_decimais(self):
        self.assertEqual(divisao(100.0, 2.5, 4), 10.0)

    def teste_divisao_misturada(self):
        self.assertEqual(divisao(100, 2.5, 4), 10.0)

    def teste_divisao_vazio(self):
        self.assertEqual(divisao(), 1)

    def teste_divisao_valor_invalido(self):
        with self.assertRaises(ValueError):
            divisao(100, 2, "a")

    def teste_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            divisao(100, 0)

    def teste_divisao_um_valor(self):
        self.assertEqual(divisao(100), 100)

    def teste_divisao_varios_valores(self):
        self.assertEqual(divisao(1000, 10, 10), 10.0)


if __name__ == "__main__":
    unittest.main()
