# Problem Statement
# https://adventofcode.com/2019/day/7


import itertools
from AoC_2019.Common.Computer import Computer


def read_input_file(file):
    with open(file) as file:
        return [int(element) for element in file.read().split(",")]


def feedback_thruster_output(instructions):
    output_signals = []
    permutations = list(itertools.permutations(range(5, 10)))

    for phases in permutations:
        input_val = feedback_amplifier(instructions, phases)
        output_signals.append(input_val)
    return max(output_signals)


def feedback_amplifier(instructions, phases):
    computers = [Computer(instructions) for _ in range(5)]
    halted = [False] * 5
    amp_index = 0
    input_val = 0
    in_phase = False
    for i in range(5):
        while not halted[i]:
            output, halted[i] = computers[amp_index].execute(input_val, True, in_phase, phases[amp_index], True)
            input_val = output
            amp_index = (amp_index + 1) % 5

            if amp_index == 0:
                in_phase = True
    return input_val


def thruster_output(instructions):
    output_signals = []
    permutations = list(itertools.permutations(range(5)))
    for phases in permutations:
        output_signals.append(amplifier(instructions, phases))
    return max(output_signals)


def amplifier(instructions, phases):
    input_val = 0
    for phase in phases:
        input_val = Computer(instructions).execute(input_val, True, False, phase)[0]
    return input_val


assert amplifier([3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0], (4, 3, 2, 1, 0)) == 43210
assert amplifier([3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23,
                  101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0], (0, 1, 2, 3, 4)) == 54321
assert amplifier([3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
                  1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0], (1, 0, 4, 3, 2)) == 65210
assert feedback_amplifier([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
                           27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5], (9, 8, 7, 6, 5)) == 139629729
assert feedback_amplifier([3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
                           -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
                           53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10], (9, 7, 8, 5, 6)) == 18216

print("Part 1 ans", thruster_output(read_input_file("Files/day-7-input.txt")))
print("Part 2 ans", feedback_thruster_output(read_input_file("Files/day-7-input.txt")))
