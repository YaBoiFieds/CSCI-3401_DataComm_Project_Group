import unittest
from archive.SurvivableLeastCostPath import *

class RemoveEdgeTest(unittest.TestCase):
    def test_removeEdge_accurate(self):
        # set up
        testGraph = MakeGraph({'a', 'b', 'c'}, {('a', 'b'), ('a', 'c')})
        testGraph.removeEdge('a', 'b')

        # assert statements
        self.assertEqual(testGraph.e_amnt(), 1)

        print("Edge removed, amount of vertices and edges accurate.")


if __name__ == '__main__':
    unittest.main()
