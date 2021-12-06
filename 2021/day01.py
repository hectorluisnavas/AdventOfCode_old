# Day 1: Sonar Sweep
# https://adventofcode.com/2021/day/1

import timeit

# Part One
def solutionPartOne(data):
    increase = 0

    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            increase += 1

    return increase

# Part Two
def  solutionPartTwo(data):
    increase = 0

    for i in range(1, len(data) - 2):
        if sum(data[i : i + 3]) > sum(data[i - 1 : i + 2]):
            increase += 1

    return increase
    

if __name__ == "__main__":
    with open('2021/input-day01.txt') as file:
        data = [int(line.strip()) for line in file]

    startTime = timeit.default_timer()
    print('Part 1 =>', solutionPartOne(data))
    print('Part 1 Exec Time: %.1f ms' % (1000 * (timeit.default_timer() - startTime)))

    startTime = timeit.default_timer()
    print('Part 2 =>', solutionPartTwo(data))
    print('Part 2 Exec Time: %.1f ms' % (1000 * (timeit.default_timer() - startTime)))
