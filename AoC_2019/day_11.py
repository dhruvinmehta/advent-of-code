# Problem Statement
# https://adventofcode.com/2019/day/11

from AoC_2019.Common.Computer import Computer


class Robot:
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, computer, start_panel=0):
        self.panels = {(0, 0): start_panel}
        self.dx = 0
        self.position = (0, 0)
        self.output = []
        self.computer = computer
        self.computer.set_input(start_panel)

    def paint_panel(self):
        if len(self.output) % 2 == 0:
            self.panels[self.position] = self.output[-2]
            self.dx = (self.dx + (1 if self.output[-1] else -1)) % len(Robot.DIRECTIONS)
            self.position = (self.position[0] + Robot.DIRECTIONS[self.dx][0],
                             self.position[1] + self.DIRECTIONS[self.dx][1])
            self.computer.set_input(self.input_value())

    def input_value(self):
        return self.panels[self.position] if self.position in self.panels else 0


def read_input_file(file):
    with open(file) as file:
        return [int(element) for element in file.read().split(",")]


def unique_painted_panels(instructions):
    robot = Robot(Computer(instructions, True))
    while not robot.computer.halted():
        robot.output.append(robot.computer.execute())
        robot.paint_panel()
    return len(robot.panels)


def registration_number(instructions):
    robot = Robot(Computer(instructions, True), 1)
    while not robot.computer.halted():
        robot.output.append(robot.computer.execute())
        robot.paint_panel()
    image = [[" "] * 50 for _ in range(6)]
    for panel in robot.panels:
        image[panel[0]][panel[1]] = '#' if robot.panels[panel] else ' '
    return image


def solution():
    print("Part 1 ans", unique_painted_panels(read_input_file("Files/day-11-input.txt")))
    print("Part 2 ans\n")
    for row in registration_number(read_input_file("Files/day-11-input.txt")):
        print(" ".join(row))


solution()
