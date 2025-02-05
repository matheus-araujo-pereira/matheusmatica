import unittest
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../matematica_basica")),
)

from subtracao import subtracao


class TestSubtracao(unittest.TestCase):

    def teste_subtracao_inteiros(self):
        self.assertEqual(subtracao(10, 2, 3), 5)

    def teste_subtracao_decimais(self):
        self.assertEqual(subtracao(10.5, 2.5, 3.0), 5.0)

    def teste_subtracao_misturada(self):
        self.assertEqual(subtracao(10, 2.5, 3), 4.5)

    def teste_subtracao_vazio(self):
        self.assertEqual(subtracao(), 0)

    def teste_subtracao_valor_invalido(self):
        with self.assertRaises(ValueError):
            subtracao(10, 2, "a")

    def teste_subtracao_um_valor(self):
        self.assertEqual(subtracao(10), 10)

    def teste_subtracao_varios_valores(self):
        self.assertEqual(subtracao(100, 10, 20, 30, 40), 0)


if __name__ == "__main__":
    unittest.main()
