from agente import Agente
import unittest

class TestPractice(unittest.TestCase):
    def testA(self):
        agente = Agente()
        res = agente.solucion_problema_rompecabeza_lineal([2,4,1,3])
        self.assertEqual([1,2,3,4], res)

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
