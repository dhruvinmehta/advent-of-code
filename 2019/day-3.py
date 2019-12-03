# Problem Statement
# https://adventofcode.com/2019/day/3


def read_input_file(file):
    wires = []
    with open(file) as file:
        line = file.readline()
        while line:
            wires.append(line.split(","))
            line = file.readline()
    return wires


def create_points(wire):
    direction_diff = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    points = {}
    prev_point = (0, 0)
    distance = 0
    for path in wire:
        diff = direction_diff.get(path[0])
        for _ in range(int(path[1:])):
            prev_point = (prev_point[0] + diff[0], prev_point[1] + diff[1])
            distance += 1
            points[prev_point] = distance
    return points


def nearest_intersection_and_distance(wire1, wire2):
    points1 = create_points(wire1)
    points2 = create_points(wire2)

    intersecting_points = points1.keys() & points2.keys()

    nearest_intersection = min([abs(point[0]) + abs(point[1]) for point in intersecting_points])
    nearest_intersection_distance = min([points1[point] + points2[point] for point in intersecting_points])

    return nearest_intersection, nearest_intersection_distance


# Unit tests
assert nearest_intersection_and_distance(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']) == (6, 30)
assert nearest_intersection_and_distance(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                                         ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']) == (159, 610)
assert nearest_intersection_and_distance(
                                    ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
                                    ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']) == (135, 410)


def solution():
    wires = read_input_file("Files/day-3-input.txt")
    result = nearest_intersection_and_distance(wires[0], wires[1])
    print("Part 1 ans", result[0])
    print("Part 2 ans", result[1])


solution()
