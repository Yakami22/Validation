import unittest

from model.DictGraph import DictGraph
from model.Hanoi import HanoiConfiguration, HanoiRules
from model.NBits import NBits


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dictGraph = DictGraph({1: [2, 3], 2: [5, 6], 3: [], 4: [4, 6], 5: [4], 6: [6]}, [])
        self.nBits = NBits([0, 1, 2], 3)
        self.hanoiConfiguration = HanoiConfiguration(3, 4)
        self.hanoi = HanoiRules([[3, 1], [2], []])

    def test_dictGraph(self):
        self.assertEqual(self.dictGraph.next(1), [2, 3])
        self.assertEqual(self.dictGraph.next(3), [])

    def test_nBits(self):
        self.assertIn(1, self.nBits.next(3))
        self.assertIn(2, self.nBits.next(3))
        self.assertIn(7, self.nBits.next(3))
        self.assertNotIn(3, self.nBits.next(3))

    def test_hanoi(self):
        self.assertIn([[3, 1], [2], []], self.hanoi.next([[3, 1], [2], []]))
        self.assertIn([[3], [2, 1], []], self.hanoi.next([[3, 1], [2], []]))
        self.assertIn([[3], [2], [1]], self.hanoi.next([[3, 1], [2], []]))
        self.assertIn([[3, 1], [], [2]], self.hanoi.next([[3, 1], [2], []]))
        self.assertNotIn([[3, 2, 1], [], []], self.hanoi.next([[3, 1], [2], []]))


if __name__ == '__main__':
    unittest.main()
