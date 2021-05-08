import unittest
from archive.SurvivableLeastCostPath import *

class DegreeTestCase(unittest.TestCase):
    def test_degree_accurate(self):

        # set up
        testGraph = MakeGraph({'a', 'b', 'c'}, {('a', 'b'), ('a', 'c')})

        # assert statements
        self.assertEqual(testGraph.degree('a'), 2, 'Broken somewhere.')
        self.assertEqual(testGraph.degree('b'), 1, 'Broken somewhere')
        self.assertEqual(testGraph.degree('c'), 1, 'Broken somewhere.')

        print("Degree method accurate.")

if __name__ == '__main__':
    unittest.main()
