# Day 3: Binary Diagnostic
# https://adventofcode.com/2021/day/3

import timeit

# Part One
def solutionPartOne(data):
    gamma_rate = 0
    nBits = max(line.bit_length() for line in data)
    
    for i in range(nBits):
        gamma_bit =  sum((x >> i) & 1 for x in data) > len(data) // 2
        gamma_rate |= gamma_bit << i

    epsilon_rate = gamma_rate ^ int("1" * nBits, 2)
    power_consumption = gamma_rate * epsilon_rate

    return power_consumption

# Part Two
def solutionPartTwo(data):
    o2_data = data.copy()
    co2_data = data.copy()
    nBits = max(line.bit_length() for line in data)

    for i in range(nBits):
        o2_bit = sum((x >> (nBits - i)) & 1 for x in o2_data) >= len(o2_data) / 2
        o2_data = [x for x in o2_data if (x >> (nBits - i)) & 1 == o2_bit] or o2_data

    for i in range(nBits):
        co2_bit = sum((x >> (nBits - i)) & 1 for x in co2_data) < len(co2_data) / 2
        co2_data = [x for x in co2_data if (x >> (nBits - i)) & 1 == co2_bit] or co2_data
    
    life_support_rate = o2_data[0] * co2_data[0]

    return life_support_rate
        
if __name__ == "__main__":
    with open('2021/input-day03.txt') as file:
        data = [int(line, 2) for line in file]
        
    startTime = timeit.default_timer()
    print('Part 1 =>', solutionPartOne(data))
    print('Part 1 Exec Time: %.1f ms' % (1000 * (timeit.default_timer() - startTime)))

    startTime = timeit.default_timer()
    print('Part 2 =>', solutionPartTwo(data))
    print('Part 2 Exec Time: %.1f ms' % (1000 * (timeit.default_timer() - startTime)))