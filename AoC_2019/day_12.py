# Problem Statement
# https://adventofcode.com/2019/day/12


def velocity(positions, velocities, dimension):
    negative = -1
    for first in range(len(positions)):
        for second in range(first + 1, len(positions)):
            if positions[first][dimension] != positions[second][dimension]:
                number = 1 if positions[first][dimension] > positions[second][dimension] else -1
                velocities[first][dimension] += number * negative
                velocities[second][dimension] += number


def position(positions, velocities, dimension):
    for index in range(len(positions)):
        positions[index][dimension] += velocities[index][dimension]


def energy(positions, steps):
    total = 0
    velocities = [[0, 0, 0] for _ in range(len(positions))]
    for step in range(steps):
        for dimension in range(3):
            velocity(positions, velocities, dimension)
            position(positions, velocities, dimension)

    for i in range(len(positions)):
        total += sum([abs(positions[i][d]) for d in range(3)]) * sum([abs(velocities[i][d]) for d in range(3)])
    return total


def simulate(positions):
    x = first_repetition(positions[:], 0)
    y = first_repetition(positions[:], 1)
    z = first_repetition(positions[:], 2)
    return lcm(lcm(x, y), z)


def lcm(num1, num2):
    a, b = num1, num2
    while a:
        a, b = b % a, a
    return num1 // b * num2


def first_repetition(positions, dimension):
    index = 0
    velocities = [[0, 0, 0] for _ in range(len(positions))]
    visited = set()
    while True:
        velocity(positions, velocities, dimension)
        position(positions, velocities, dimension)

        point = (tuple([x[dimension] for x in positions]), tuple([x[dimension] for x in velocities]))
        if point in visited:
            return index
            break
        visited.add(point)
        index += 1


assert energy([[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]], 10) == 179
assert energy([[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]], 100) == 1940
assert simulate([[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]) == 2772
assert simulate([[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]) == 4686774924


def solution():
    print("Part 1 ans", energy([[-7, -8, 9], [-12, -3, -4], [6, -17, -9], [4, -10, -6]], 1000))
    print("Part 2 ans", simulate([[-7, -8, 9], [-12, -3, -4], [6, -17, -9], [4, -10, -6]]))


solution()
