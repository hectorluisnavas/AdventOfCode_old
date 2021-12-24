# Day 4: Giant Squid
# https://adventofcode.com/2021/day/4

import timeit
import numpy as np


class Board:
    def __init__(self, board_data):
        self.data = np.array([data.split() for data in board_data], ndmin=2)
        self.temp_data = self.data.copy()

    def mark(self, target):
        for x_index, x_value in enumerate(self.temp_data):
            for y_index, y_value in enumerate(x_value):
                if y_value == target:
                    self.temp_data[x_index][y_index] = "X"

    def check_winner(self):
        for x_value in self.temp_data:
            if len(set(x_value)) == 1:
                return True
        
        reversed_data = np.transpose(self.temp_data)
        for x_value in reversed_data:
            if len(set(x_value)) == 1:
                return True
        
        return False

    def get_score(self, last_draw):
        flatten_data = np.ravel(self.temp_data)
        score = sum(int(data) for data in flatten_data if data != "X") * int(last_draw)
        return score

    def reset(self):
        self.temp_data = self.data

# Part One
def solutionPartOne(draws, boards):
    draws_data = draws.copy()
    
    while draws_data:
        actual_draw = draws_data.pop(0)

        for board in boards:
            board.mark(actual_draw)
            if board.check_winner():
                return board.get_score(actual_draw)

# Part Two
def solutionPartTwo(draws, boards):
    draws_data = draws.copy()
    boards_data = boards.copy()

    while draws_data and boards_data:
        actual_draw = draws_data.pop(0)

        for board in boards_data:
            board.mark(actual_draw)
        
        for board_index, board in enumerate(boards_data):
            if board.check_winner():
                winner = boards_data.pop(board_index)
    
    return winner.get_score(actual_draw)

if __name__ == "__main__":
    with open('2021/input-day04.txt') as file:
        data = file.read().splitlines()
    
    draws = data[0].split(',')
    boards = [Board(data[i + 1 : i + 6]) for i, line in enumerate(data) if line == "" ]

    startTime = timeit.default_timer()
    print('Part 1 =>', solutionPartOne(draws, boards))
    print('Part 1 Exec Time: %.1f ms' % (1000 * (timeit.default_timer() - startTime)))

    for board in boards:
        board.reset()
    
    startTime = timeit.default_timer()
    print('Part 2 =>', solutionPartTwo(draws, boards))
    print('Part 2 Exec Time: %.1f ms' % (1000 * (timeit.default_timer() - startTime)))