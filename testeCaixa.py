import unittest
from caixa import Caixa

class TesteCaixa(unittest.TestCase):

    def setUp(self):
        self.caixa = Caixa()
    
    def testeAbastecer(self):
        self.caixa.abastecerCaixa(10, 1)
        self.assertEqual(self.caixa._Caixa__notas["10"], 1)

    def testeSaqueSimples(self):
        self.caixa.abastecerCaixa(10, 1)
        self.caixa.sacarQuantia(10)
        self.assertEqual(self.caixa._Caixa__notas["10"], 0)

    def testeSaqueMaiorMenor(self):
        self.caixa.abastecerCaixa(10, 1)
        self.caixa.abastecerCaixa(20, 1)
        self.caixa.abastecerCaixa(50, 1)
        self.caixa.sacarQuantia(70)
        self.assertEqual(self.caixa._Caixa__notas, {"10": 1,"20": 0,"50": 0,"100": 0})

    def testeSaqueMenorMaior(self):
        self.caixa.abastecerCaixa(20, 3)
        self.caixa.abastecerCaixa(50, 1)
        self.caixa.abastecerCaixa(100, 1)
        self.caixa.sacarQuantia(110)
        self.assertEqual(self.caixa._Caixa__notas, {"10": 0,"20": 0,"50": 0,"100": 1})

    def testeSaquePulaValor(self):
        self.caixa.abastecerCaixa(20, 3)
        self.caixa.abastecerCaixa(50, 1)
        self.caixa.abastecerCaixa(100, 1)
        self.caixa.sacarQuantia(160)
        self.assertEqual(self.caixa._Caixa__notas, {"10": 0,"20": 0,"50": 1,"100": 0})

if __name__ == '__main__':
    unittest.main()