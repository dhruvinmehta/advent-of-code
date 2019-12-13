# Problem Statement
# https://adventofcode.com/2019/day/8


def read_input_file(file):
    with open(file) as file:
        return file.read()


def part1_ans(pixels, width, height):
    layers = get_layers(pixels, width, height)
    min_zero_layer = min(layers, key=lambda x: x.count(0))
    return min_zero_layer.count(1) * min_zero_layer.count(2)


def get_layers(pixels, width, height):
    layers = [None] * (len(pixels) // (width * height))
    for i in range(len(layers)):
        layers[i] = [int(pixel) for pixel in pixels[i * width * height: (i + 1) * width * height]]
    return layers


def password_image(pixels, width, height):
    layers = get_layers(pixels, width, height)
    image = []

    for layer in zip(*layers):
        for pixel in layer:
            if pixel != 2:
                image.append(' ' if pixel == 0 else '#')
                break

    result = ''
    for i in range(height):
        result += ' '.join(image[i * width: (i + 1) * width]) + "\n"
    return result


# Unit tests
assert get_layers("123456789012", 3, 2) == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 1, 2]]
assert password_image("0222112222120000", 2, 2) == '  #\n#  \n'


def solution():
    print("Part 1 ans", part1_ans(read_input_file("Files/day-8-input.txt"), 25, 6))
    print("Part 2 ans")
    print(password_image(read_input_file("Files/day-8-input.txt"), 25, 6))


solution()
