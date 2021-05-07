import unittest
from SurvivableLeastCostPath import *

class NbrsTestCase(unittest.TestCase):
    def test_nbrs_accurate(self):
        # set up
        testGraph = MakeGraph({'a', 'b', 'c'}, {('a', 'b'), ('a', 'c')})

        # assert statements
        self.assertEqual(list(testGraph.nbrs('a')), ['b', 'c'])
        self.assertEqual(list(testGraph.nbrs('b')), ['a'])

        print("Shows correct neighbors.")


if __name__ == '__main__':
    unittest.main()
