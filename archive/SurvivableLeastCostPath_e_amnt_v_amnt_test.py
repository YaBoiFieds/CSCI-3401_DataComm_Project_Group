import unittest
from archive.SurvivableLeastCostPath import *

class EAmntVAmntTestCase(unittest.TestCase):
    def test_v_amnt_accurate(self):
        # set up
        testGraph = MakeGraph({'a', 'b', 'c'}, {('a', 'b'), ('a', 'c')})

        # assert statements
        self.assertEqual(testGraph.e_amnt(), 2)
        self.assertEqual(testGraph.v_amnt(), 3)

        print("Amount of vertices and edges accurate.")


if __name__ == '__main__':
    unittest.main()
