# Problem Statement
# https://adventofcode.com/2019/day/5


def read_input_file(file):
    with open(file) as file:
        return [int(element) for element in file.read().split(",")]


def value(instructions, index, mode):
    if mode == 0:
        return instructions[instructions[index]]
    else:
        return instructions[index]


def decode(opcode):
    opcode_str = str(opcode).zfill(4)
    return int(opcode_str[1]), int(opcode_str[0]), int(opcode_str[-2:])


def opcode1(instructions, index, **kwargs):
    instructions[instructions[index + 3]] = value(instructions, index + 1, kwargs.get('mode1')) + value(instructions, index + 2, kwargs.get('mode2'))
    return index + 4


def opcode2(instructions, index, **kwargs):
    instructions[instructions[index + 3]] = value(instructions, index + 1, kwargs.get('mode1')) * value(instructions, index + 2, kwargs.get('mode2'))
    return index + 4


def opcode3(instructions, index, **kwargs):
    instructions[instructions[index + 1]] = kwargs.get('input_val')
    return index + 2


def opcode4(instructions, index, **kwargs):
    kwargs.get('outputs').append(value(instructions, index + 1, kwargs.get('mode1')))
    return index + 2


def opcode5(instructions, index, **kwargs):
    if value(instructions, index + 1, kwargs.get('mode1')) != 0:
        return value(instructions, index + 2, kwargs.get('mode2'))
    else:
        return index + 3


def opcode6(instructions, index, **kwargs):
    if value(instructions, index + 1, kwargs.get('mode1')) == 0:
        return value(instructions, index + 2, kwargs.get('mode2'))
    else:
        return index + 3


def opcode7(instructions, index, **kwargs):
    if value(instructions, index + 1, kwargs.get('mode1')) < value(instructions, index + 2, kwargs.get('mode2')):
        instructions[instructions[index + 3]] = 1
    else:
        instructions[instructions[index + 3]] = 0
    return index + 4


def opcode8(instructions, index, **kwargs):
    if value(instructions, index + 1, kwargs.get('mode1')) == value(instructions, index + 2, kwargs.get('mode2')):
        instructions[instructions[index + 3]] = 1
    else:
        instructions[instructions[index + 3]] = 0
    return index + 4


OPCODE_MAP = {1: opcode1, 2: opcode2, 3: opcode3, 4: opcode4, 5: opcode5, 6: opcode6, 7: opcode7, 8: opcode8}


def execute(instructions, input_val=1):
    outputs = []
    index = 0
    while instructions[index] != 99:
        mode1, mode2, opcode = decode(instructions[index])
        index = OPCODE_MAP[opcode](instructions, index, mode1=mode1, mode2=mode2, input_val=input_val, outputs=outputs)

    return outputs


# Unit tests
assert execute([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 8) == [1]
assert execute([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], 3) == [0]
assert execute([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 5) == [1]
assert execute([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], 8) == [0]
assert execute([3, 3, 1108, -1, 8, 3, 4, 3, 99], 8) == [1]
assert execute([3, 3, 1108, -1, 8, 3, 4, 3, 99], 10) == [0]
assert execute([3, 3, 1107, -1, 8, 3, 4, 3, 99], 6) == [1]
assert execute([3, 3, 1107, -1, 8, 3, 4, 3, 99], 9) == [0]
assert execute([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 0) == [0]
assert execute([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], 5) == [1]
assert execute([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 0) == [0]
assert execute([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], 8) == [1]


def solution():
    print("Part 1 ans", execute(read_input_file("Files/day-5-input.txt"))[-1])
    print("Part 2 ans", execute(read_input_file("Files/day-5-input.txt"), 5)[-1])


solution()
