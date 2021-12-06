import unittest
from day01 import solutionPartOne as sp1
from day01 import solutionPartTwo as sp2

class TestDay01(unittest.TestCase):
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_partOne(self):
        result = 7
        self.assertEqual(sp1(self.data), result)

    def test_partTwo(self):
        result = 5
        self.assertEqual(sp2(self.data), result)

if __name__ == '__main__':
    unittest.main()