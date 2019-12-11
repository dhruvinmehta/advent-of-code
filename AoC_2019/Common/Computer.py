class Computer:
    """ Intcode computer"""
    def __init__(self, instructions):
        self.instructions = instructions[:]
        self.pointer = 0
        self.output = []
        self.relative_base = 0
        self.painting_robot = False
        self.panels = {}
        self.position = (0, 0)
        self.dx = 0

    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def make_painting_robot(self, start_panel=0):
        self.painting_robot = True
        self.panels = {(0, 0): start_panel}
        return self

    def mem_address(self, offset, mode):
        pointer = 0
        if mode == 0:
            pointer = self.instructions[self.pointer + offset]
        elif mode == 1:
            pointer = self.pointer + offset
        elif mode == 2:
            pointer = self.relative_base + self.instructions[self.pointer + offset]
        self.increase(pointer)
        return pointer

    def increase(self, index):
        while index > len(self.instructions) - 1:
            self.instructions.append(0)

    @staticmethod
    def decode(opcode):
        opcode_str = str(opcode).zfill(5)
        return int(opcode_str[2]), int(opcode_str[1]), int(opcode_str[0]), int(opcode_str[-2:])

    def first_pos(self, kwargs):
        return self.instructions[self.mem_address(1, kwargs.get('mode1'))]

    def second_pos(self, kwargs):
        return self.instructions[self.mem_address(2, kwargs.get('mode2'))]

    def opcode1(self, **kwargs):
        self.instructions[self.mem_address(3, kwargs.get('mode3'))] = self.first_pos(kwargs) + self.second_pos(kwargs)
        self.pointer += 4

    def opcode2(self, **kwargs):
        self.instructions[self.mem_address(3, kwargs.get('mode3'))] = self.first_pos(kwargs) * self.second_pos(kwargs)
        self.pointer += 4

    def opcode3(self, **kwargs):
        self.instructions[self.mem_address(1, kwargs.get('mode1'))] = kwargs.get('input_val')
        self.pointer += 2

    def opcode4(self, **kwargs):
        self.output.append(self.first_pos(kwargs))
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
            self.instructions[self.mem_address(3, kwargs.get('mode3'))] = 1
        else:
            self.instructions[self.mem_address(3, kwargs.get('mode3'))] = 0
        self.pointer += 4

    def opcode8(self, **kwargs):
        if self.first_pos(kwargs) == self.second_pos(kwargs):
            self.instructions[self.mem_address(3, kwargs.get('mode3'))] = 1
        else:
            self.instructions[self.mem_address(3, kwargs.get('mode3'))] = 0
        self.pointer += 4

    def opcode9(self, **kwargs):
        self.relative_base += self.first_pos(kwargs)
        self.pointer += 2

    OPCODE_MAP = {1: opcode1, 2: opcode2, 3: opcode3, 4: opcode4, 5: opcode5, 6: opcode6, 7: opcode7,
                  8: opcode8, 9: opcode9}

    def execute(self, input_val=1, is_amplifier=False, in_phase=False, phase_val=0, feedback=False):
        while self.instructions[self.pointer] != 99:
            mode1, mode2, mode3, opcode = self.decode(self.instructions[self.pointer])

            temp_val = self.get_input_value(in_phase, input_val, is_amplifier, phase_val)
            Computer.OPCODE_MAP[opcode](self, mode1=mode1, mode2=mode2, mode3=mode3, input_val=temp_val)

            if opcode == 3 and is_amplifier:
                in_phase = True

            if opcode == 4:
                self.paint_panel()
                if feedback:
                    return self.output[-1], False

        return self.output[-1], True

    def paint_panel(self):
        if self.painting_robot and len(self.output) % 2 == 0:
            self.panels[self.position] = self.output[-2]
            self.dx = (self.dx + (1 if self.output[-1] else -1)) % len(Computer.DIRECTIONS)
            self.position = (self.position[0] + Computer.DIRECTIONS[self.dx][0],
                             self.position[1] + Computer.DIRECTIONS[self.dx][1])

    def get_input_value(self, in_phase, input_val, is_amplifier, phase_val):
        if self.painting_robot:
            return self.panels[self.position] if self.position in self.panels else 0
        else:
            return input_val if in_phase else phase_val if is_amplifier else input_val


