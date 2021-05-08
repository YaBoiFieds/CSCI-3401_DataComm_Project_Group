import unittest
from archive.SurvivableLeastCostPath import *

class AddEdgeTestCase(unittest.TestCase):
    def test_addEdge_works(self):
        # set up
        testGraph = MakeGraph({'a', 'b', 'c'}, {('a', 'b'), ('a', 'c')})
        testGraph.addEdge('d', 'b')

        # assert statements
        self.assertEqual(testGraph.degree('a'), 2, 'Broken somewhere.')
        self.assertEqual(testGraph.degree('b'), 2, 'Broken somewhere')
        self.assertEqual(testGraph.degree('c'), 1, 'Broken somewhere.')
        self.assertEqual(testGraph.degree('d'), 1, 'Broken somewhere.')

        print("Edge added correctly.")

if __name__ == '__main__':
    unittest.main()
