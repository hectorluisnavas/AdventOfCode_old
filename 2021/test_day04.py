import unittest
from day04 import solutionPartOne as sp1
from day04 import solutionPartTwo as sp2

class TestDay04(unittest.TestCase):
    draws = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
    boards = [[22, 13, 17, 11, 0],[8, 2, 23, 4, 24],[21, 9, 14, 16, 7],[6, 10, 3, 18, 5],[1, 12, 20, 15, 19]],[[3, 15, 0, 2, 22],[9, 18, 13, 17, 5],[19, 8, 7, 25, 23],[20, 11, 10, 24, 4],[14, 21, 16, 12, 6]],[[14, 21, 17, 24, 4],[10, 16, 15, 9, 19],[18, 8, 23, 26, 20],[22, 11, 13, 6, 5],[2, 0, 12, 3, 7]]

    def test_partOne(self):
        result = 4512
        self.assertEqual(sp1(self.draws, self.boards), result)

    def test_partTwo(self):
        result = 1924
        self.assertEqual(sp2(self.draws, self.boards), result)

if __name__ == '__main__':
    unittest.main()