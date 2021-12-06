# Day 2: Dive!
# https://adventofcode.com/2021/day/2

import timeit
    
# Part One
def solutionPartOne(data):
    horizontal = depth = 0
    moves = [[move[0], int(move[1])] for move in data]

    for move in moves:
        if move[0] == 'forward':
            horizontal += move[1]
        if move[0] == 'down':
            depth += move[1]
        if move[0] == 'up':
            depth -= move[1]
    
    product = horizontal * depth

    print('Part 1 => Horizontal:', horizontal, '| Depth:', depth)

    return product

# Part Two
def solutionPartTwo(data):
    horizontal = depth = aim = 0
    moves = [[move[0], int(move[1])] for move in data]

    for move in moves:
        if move[0] == 'forward':
            horizontal += move[1]
            depth += aim * move[1]
        if move[0] == 'down':
            aim += move[1]
        if move[0] == 'up':
            aim -= move[1]
    
    product = horizontal * depth

    print('Part 2 => Horizontal:', horizontal, '| Depth:', depth, '| Aim:', aim)

    return product

if __name__ == "__main__":
    with open('2021/input-day02.txt') as file:
        data = [line.split() for line in file]

    startTime = timeit.default_timer()
    print('Part 1 =>', solutionPartOne(data))
    print('Part 1 Exec Time: %.1f ms' % (1000 * (timeit.default_timer() - startTime)))

    startTime = timeit.default_timer()
    print('Part 2 =>', solutionPartTwo(data))
    print('Part 2 Exec Time: %.1f ms' % (1000 * (timeit.default_timer() - startTime)))