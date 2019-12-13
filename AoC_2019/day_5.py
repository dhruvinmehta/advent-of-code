# Problem Statement
# https://adventofcode.com/2019/day/5


from AoC_2019.Common.Computer import Computer


def read_input_file(file):
    with open(file) as file:
        return [int(element) for element in file.read().split(",")]


# Unit tests
assert Computer([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]).execute(8) == 1
assert Computer([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]).execute(3) == 0
assert Computer([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]).execute(5) == 1
assert Computer([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]).execute(8) == 0
assert Computer([3, 3, 1108, -1, 8, 3, 4, 3, 99]).execute(8) == 1
assert Computer([3, 3, 1108, -1, 8, 3, 4, 3, 99]).execute(10) == 0
assert Computer([3, 3, 1107, -1, 8, 3, 4, 3, 99]).execute(6) == 1
assert Computer([3, 3, 1107, -1, 8, 3, 4, 3, 99]).execute(9) == 0
assert Computer([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]).execute(0) == 0
assert Computer([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]).execute(5) == 1
assert Computer([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]).execute(0) == 0
assert Computer([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]).execute(8) == 1


def solution():
    print("Part 1 ans", Computer(read_input_file("Files/day-5-input.txt")).execute())
    print("Part 2 ans", Computer(read_input_file("Files/day-5-input.txt")).execute(5))


solution()
