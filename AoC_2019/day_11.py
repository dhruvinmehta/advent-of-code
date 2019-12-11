# Problem Statement
# https://adventofcode.com/2019/day/11

from AoC_2019.Common.Computer import Computer


def read_input_file(file):
    with open(file) as file:
        return [int(element) for element in file.read().split(",")]


def solution():
    computer = Computer(read_input_file("Files/day-11-input.txt")).make_painting_robot()
    computer.execute()
    print("Part 1 ans", len(computer.panels))
    computer = Computer(read_input_file("Files/day-11-input.txt")).make_painting_robot(1)
    computer.execute()
    print("Part 2 ans\n")
    image = [[" "] * 50 for _ in range(6)]
    for panel in computer.panels:
        image[panel[0]][panel[1]] = '#' if computer.panels[panel] else ' '
    for row in image:
        print(" ".join(row))


solution()
