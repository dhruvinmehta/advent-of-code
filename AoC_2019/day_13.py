# Problem Statement
# https://adventofcode.com/2019/day/13

from AoC_2019.Common.Computer import Computer


def read_input_file(file):
    with open(file) as file:
        return [int(element) for element in file.read().split(",")]


def block_tiles(instructions):
    count = 0
    output = []
    computer = Computer(instructions, True)
    while not computer.halted():
        output.append(computer.execute())
        if len(output) % 3 == 0:
            count += 1 if output[-1] == 2 else 0
    return count


def score(instructions):
    instructions[0] = 2
    output = []
    game_score = 0
    paddle = ball = None
    computer = Computer(instructions, True)
    while not computer.halted():
        computer.set_input(max(-1, min(ball - paddle, 1)) if paddle and ball else 0, True)
        output.append(computer.execute(0))

        if len(output) % 3 == 0:
            paddle = output[-3] if output[-1] == 3 else paddle
            ball = output[-3] if output[-1] == 4 else ball
            game_score = output[-1] if (output[-3], output[-2]) == (-1, 0) else game_score
    return game_score


def solution():
    print("Part 1 ans", block_tiles(read_input_file("Files/day-13-input.txt")))
    print("Part 2 ans", score(read_input_file("Files/day-13-input.txt")))


solution()
