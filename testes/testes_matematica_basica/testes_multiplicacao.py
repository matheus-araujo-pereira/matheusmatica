import unittest
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../matematica_basica")),
)

from multiplicacao import multiplicacao


class TestMultiplicacao(unittest.TestCase):

    def teste_multiplicacao_inteiros(self):
        self.assertEqual(multiplicacao(2, 3, 4), 24)

    def teste_multiplicacao_decimais(self):
        self.assertEqual(multiplicacao(1.5, 2.0, 3), 9.0)

    def teste_multiplicacao_misturada(self):
        self.assertEqual(multiplicacao(2, 2.5, 4), 20.0)

    def teste_multiplicacao_vazio(self):
        self.assertEqual(multiplicacao(), 1)

    def teste_multiplicacao_valor_invalido(self):
        with self.assertRaises(ValueError):
            multiplicacao(2, 3, "a")

    def teste_multiplicacao_um_valor(self):
        self.assertEqual(multiplicacao(5), 5)

    def teste_multiplicacao_varios_valores(self):
        self.assertEqual(multiplicacao(1, 2, 3, 4, 5), 120)


if __name__ == "__main__":
    unittest.main()
