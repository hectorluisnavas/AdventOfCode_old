# Day 1: Sonar Sweep
# https://adventofcode.com/2021/day/1

with open("2021/input-day01.txt") as file:
    fileData = [int(line.strip()) for line in file]

# Part One
def solutionPartOne(data):
    increase = 0

    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            increase += 1
    
    print(increase)

# Part Two
def  solutionPartTwo(data):
    increase = 0

    for i in range(1, len(data) - 2):
        if sum(data[i : i + 3]) > sum(data[i - 1 : i + 2]):
            increase += 1

    print(increase) 

solutionPartOne(fileData)
solutionPartTwo(fileData)
