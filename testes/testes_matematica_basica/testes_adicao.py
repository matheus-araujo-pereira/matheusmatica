import unittest
import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../matematica_basica")),
)

from adicao import adicao


class TestAdicao(unittest.TestCase):

    def teste_adicao_inteiros(self):
        self.assertEqual(adicao(1, 2, 3, 4), 10)

    def teste_adicao_decimais(self):
        self.assertEqual(adicao(1.5, 2.5, 3.5, 4.5), 12)

    def teste_adicao_misturada(self):
        self.assertEqual(adicao(1, 2.5, 3, 4.5), 11)

    def teste_adicao_vazio(self):
        self.assertEqual(adicao(), 0)

    def teste_adicao_valor_invalido(self):
        with self.assertRaises(ValueError):
            adicao(1, 2, "a", 4)

    def teste_adicao_um_valor(self):
        self.assertEqual(adicao(1), 1)

    def teste_adicao_varios_valores(self):
        self.assertEqual(adicao(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 55)


if __name__ == "__main__":
    unittest.main()
