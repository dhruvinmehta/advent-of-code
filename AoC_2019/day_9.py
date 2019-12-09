# Problem Statement
# https://adventofcode.com/2019/day/9


from AoC_2019.Common.Computer import Computer


def read_input_file(file):
    with open(file) as file:
        return [int(element) for element in file.read().split(",")]


# Unit tests
assert len(str(Computer([1102, 34915192, 34915192, 7, 4, 7, 99, 0]).execute()[0])) == 16
assert Computer([104, 1125899906842624, 99]).execute() == (1125899906842624, True)


def solution():
    print("Part 1 ans", Computer(read_input_file("Files/day-9-input.txt")).execute()[0])
    print("Part 2 ans", Computer(read_input_file("Files/day-9-input.txt")).execute(2)[0])


solution()
