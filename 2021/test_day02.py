import unittest
from day02 import solutionPartOne as sp1
from day02 import solutionPartTwo as sp2

class TestDay01(unittest.TestCase):
    data = [['forward', 5], ['down', 5], ['forward', 8], ['up', 3], ['down', 8], ['forward', 2]]

    def test_partOne(self):
        result = 150
        self.assertEqual(sp1(self.data), result)

    def test_partTwo(self):
        result = 900
        self.assertEqual(sp2(self.data), result)

if __name__ == '__main__':
    unittest.main()