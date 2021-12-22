import unittest
from day03 import solutionPartOne as sp1
from day03 import solutionPartTwo as sp2

class TestDay01(unittest.TestCase):
    data = [0b00100, 0b11110, 0b10110, 0b10111, 0b10101, 0b01111, 0b00111, 0b11100, 0b10000, 0b11001, 0b00010, 0b01010]

    def test_partOne(self):
        result = 198
        self.assertEqual(sp1(self.data), result)

    def test_partTwo(self):
        result = 220
        self.assertEqual(sp2(self.data), result)

if __name__ == '__main__':
    unittest.main()