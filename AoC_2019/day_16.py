# Problem Statement
# https://adventofcode.com/2019/day/16


def read_input_file(file):
    with open(file) as file:
        return file.read()


def fft(input_signal, pattern, phases):
    inputs = [int(element) for element in input_signal]
    for _ in range(phases):
        for repeat in range(len(input_signal)):
            temp = inputs[:]
            index = 1 if repeat == 0 else 0
            total = 0
            repeat_count = 1
            for i, digit in enumerate(temp):
                total += digit * pattern[index]
                repeat_count += 1
                if repeat_count >= repeat + 1:
                    index = (index + 1) % 4
                    repeat_count = 0
            inputs[repeat] = abs(total) % 10
    return ''.join(str(x) for x in inputs)


assert fft("12345678", [0, 1, 0, -1], 4) == "01029498"
assert fft("80871224585914546619083218645595", [0, 1, 0, -1], 100)[0:8] == "24176176"
assert fft("19617804207202209144916044189917", [0, 1, 0, -1], 100)[0:8] == "73745418"
assert fft("69317163492948606335995924319873", [0, 1, 0, -1], 100)[0:8] == "52432133"


def solution():
    print("Part 1 ans", fft(read_input_file("Files/day-16-input.txt"), [0, 1, 0, -1], 100)[0:8])


solution()
