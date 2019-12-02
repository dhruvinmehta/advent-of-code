# Problem Statement
# https://adventofcode.com/2019/day/2


def read_input_file(file):
    with open(file) as file:
        return [int(element) for element in file.read().split(",")]


def execute(instructions):
    index = 0
    while instructions[index] != 99:
        if instructions[index] == 1:
            instructions[instructions[index + 3]] = instructions[instructions[index + 1]] + instructions[instructions[index + 2]]
        elif instructions[index] == 2:
            instructions[instructions[index + 3]] = instructions[instructions[index + 1]] * instructions[instructions[index + 2]]
        index += 4
    return instructions


def correct_computer(instructions, noun, verb):
    updated_instruction = instructions[:]
    updated_instruction[1] = noun
    updated_instruction[2] = verb
    return execute(updated_instruction)[0]


def find_noun_verb_for_output(instructions, output):
    for noun in range(100):
        for verb in range(100):
            if correct_computer(instructions, noun, verb) == output:
                return 100 * noun + verb


# Unit tests
assert execute([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
assert execute([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert execute([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert execute([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert execute([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def solution():
    instructions = read_input_file("Files/day-2-input.txt")
    print("Part 1 ans", correct_computer(instructions, 12, 2))
    print("Part 2 ans", find_noun_verb_for_output(instructions, 19690720))


solution()
