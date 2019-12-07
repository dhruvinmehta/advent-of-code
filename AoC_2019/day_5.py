# Problem Statement
# https://adventofcode.com/2019/day/5


def read_input_file(file):
    with open(file) as file:
        return [int(element) for element in file.read().split(",")]


class Computer:
    def __init__(self, instructions):
        self.instructions = instructions[:]
        self.pointer = 0
        self.output = 0

    def value(self, index, mode):
        if mode == 0:
            return self.instructions[self.instructions[index]]
        else:
            return self.instructions[index]

    @staticmethod
    def decode(opcode):
        opcode_str = str(opcode).zfill(4)
        return int(opcode_str[1]), int(opcode_str[0]), int(opcode_str[-2:])

    def first_pos(self, kwargs):
        return self.value(self.pointer + 1, kwargs.get('mode1'))

    def second_pos(self, kwargs):
        return self.value(self.pointer + 2, kwargs.get('mode2'))

    def opcode1(self, **kwargs):
        self.instructions[self.instructions[self.pointer + 3]] = self.first_pos(kwargs) + self.second_pos(kwargs)
        self.pointer += 4

    def opcode2(self, **kwargs):
        self.instructions[self.instructions[self.pointer + 3]] = self.first_pos(kwargs) * self.second_pos(kwargs)
        self.pointer += 4

    def opcode3(self, **kwargs):
        self.instructions[self.instructions[self.pointer + 1]] = kwargs.get('input_val')
        self.pointer += 2

    def opcode4(self, **kwargs):
        self.output = self.first_pos(kwargs)
        self.pointer += 2

    def opcode5(self, **kwargs):
        if self.first_pos(kwargs) != 0:
            self.pointer = self.second_pos(kwargs)
        else:
            self.pointer += 3

    def opcode6(self, **kwargs):
        if self.first_pos(kwargs) == 0:
            self.pointer = self.second_pos(kwargs)
        else:
            self.pointer += 3

    def opcode7(self, **kwargs):
        if self.first_pos(kwargs) < self.second_pos(kwargs):
            self.instructions[self.instructions[self.pointer + 3]] = 1
        else:
            self.instructions[self.instructions[self.pointer + 3]] = 0
        self.pointer += 4

    def opcode8(self, **kwargs):
        if self.first_pos(kwargs) == self.second_pos(kwargs):
            self.instructions[self.instructions[self.pointer + 3]] = 1
        else:
            self.instructions[self.instructions[self.pointer + 3]] = 0
        self.pointer += 4

    OPCODE_MAP = {1: opcode1, 2: opcode2, 3: opcode3, 4: opcode4, 5: opcode5, 6: opcode6, 7: opcode7, 8: opcode8}

    def execute(self, input_val=1, is_amplifier=False, in_phase=False, phase_val=0, feedback=False):
        while self.instructions[self.pointer] != 99:
            mode1, mode2, opcode = self.decode(self.instructions[self.pointer])

            temp_val = input_val if in_phase else phase_val if is_amplifier else input_val
            Computer.OPCODE_MAP[opcode](self, mode1=mode1, mode2=mode2, input_val=temp_val)

            if opcode == 3 and is_amplifier:
                in_phase = True

            if opcode == 4 and feedback:
                return self.output, False

        return self.output, True


# Unit tests
assert Computer([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]).execute(8) == (1, True)
assert Computer([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]).execute(3) == (0, True)
assert Computer([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]).execute(5) == (1, True)
assert Computer([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]).execute(8) == (0, True)
assert Computer([3, 3, 1108, -1, 8, 3, 4, 3, 99]).execute(8) == (1, True)
assert Computer([3, 3, 1108, -1, 8, 3, 4, 3, 99]).execute(10) == (0, True)
assert Computer([3, 3, 1107, -1, 8, 3, 4, 3, 99]).execute(6) == (1, True)
assert Computer([3, 3, 1107, -1, 8, 3, 4, 3, 99]).execute(9) == (0, True)
assert Computer([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]).execute(0) == (0, True)
assert Computer([3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]).execute(5) == (1, True)
assert Computer([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]).execute(0) == (0, True)
assert Computer([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]).execute(8) == (1, True)


def solution():
    print("Part 1 ans", Computer(read_input_file("Files/day-5-input.txt")).execute()[0])
    print("Part 2 ans", Computer(read_input_file("Files/day-5-input.txt")).execute(5)[0])


# Uncomment below line to execute the code
# solution()
