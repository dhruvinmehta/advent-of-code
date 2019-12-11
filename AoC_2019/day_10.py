# Problem Statement
# https://adventofcode.com/2019/day/10


import math


def read_input_file(file):
    asteroid_map = []
    with open(file) as file:
        line = file.readline()
        while line:
            asteroid_map.append(line.strip())
            line = file.readline()
        return asteroid_map


def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)


def asteroid_locations(asteroid_map):
    row_length = len(asteroid_map)
    column_length = len(asteroid_map[0])
    location = []

    for row in range(row_length):
        for column in range(column_length):
            if asteroid_map[row][column] == '#':
                location.append((column, row))

    return location


def monitoring_station(asteroid_map):
    locations = asteroid_locations(asteroid_map)
    result = 0
    station = (0, 0)
    for station_x, station_y in locations:
        visible_asteroids = set()
        for current_x, current_y in locations:
            if current_y != station_y or current_x != station_x:
                visible_asteroids.add((lowest_point(current_x, current_y, station_x, station_y)))

            if len(visible_asteroids) > result:
                result = len(visible_asteroids)
                station = station_x, station_y
    return result, station


def lowest_point(current_x, current_y, station_x, station_y):
    x_diff = current_x - station_x
    y_diff = current_y - station_y
    common = abs(gcd(x_diff, y_diff))
    return x_diff // common, y_diff // common


def theta(station, asteroid):
    if station[0] == asteroid[0]:
        return 0.0 if station[1] > asteroid[1] else 180.0
    elif station[1] == asteroid[1]:
        return 90.0 if station[0] < asteroid[0] else 270.0
    else:
        angle = math.atan(abs(asteroid[1] - station[1]) / abs(asteroid[0] - station[0])) * 180 / math.pi
        if station[0] < asteroid[0]:
            return 90.0 - angle if station[1] > asteroid[1] else 90.0 + angle
        else:
            return 270.0 + angle if station[1] > asteroid[1] else 270.0 - angle


def vaporize(asteroid_map, station_x, station_y):
    kills = 0
    targets = {}
    for x, y in asteroid_locations(asteroid_map):
        if x != station_x or y != station_y:
            angle = theta((station_x, station_y), (x, y))
            if angle in targets:
                targets.get(angle).append((x, y))
            else:
                targets[angle] = [(x, y)]

    targets = sort_targets(targets)

    while kills < len(targets):
        for angle in targets:
            points = targets.get(angle)
            if len(points) == 0:
                continue
            asteroid = points.pop(0)
            kills += 1
            if kills == 200:
                return asteroid[0] * 100 + asteroid[1]
                break


def sort_targets(targets):
    targets = {key: value for key, value in sorted(targets.items(), key=lambda item: item[0])}
    for angle in targets:
        if 0 <= angle < 90 or angle > 270:
            targets[angle] = sorted(targets.get(angle), key=lambda k: k[1], reverse=True)
        elif angle == 90:
            targets[angle] = sorted(targets.get(angle), key=lambda k: k[0])
        elif 90 < angle < 270:
            targets[angle] = sorted(targets.get(angle), key=lambda k: k[1])
        elif angle == 270:
            targets[angle] = sorted(targets.get(angle), key=lambda k: k[0], reverse=True)
    return targets


# Unit tests
assert monitoring_station(["......#.#.", "#..#.#....", "..#######.", ".#.#.###..", ".#..#.....", "..#....#.#",
                           "#..#....#.", ".##.#..###", "##...#..#.", ".#....####"]) == (33, (5, 8))
assert monitoring_station(["#.#...#.#.", ".###....#.", ".#....#...", "##.#.#.#.#", "....#.#.#.", ".##..###.#",
                           "..#...##..", "..##....##", "......#...", ".####.###."]) == (35, (1, 2))
assert monitoring_station([".#..#..###", "####.###.#", "....###.#.", "..###.##.#", "##.##.#.#.", "....###..#",
                           "..#.#..#.#", "#..#.#.###", ".##...##.#", ".....#.#.."]) == (41, (6, 3))
assert monitoring_station([".#..##.###...#######", "##.############..##.", ".#.######.########.#",
                           ".###.#######.####.#.", "#####.##.#.##.###.##", "..#####..#.#########",
                           "####################", "#.####....###.#.#.##", "##.#################",
                           "#####.##.###..####..", "..######..##.#######", "####.##.####...##..#",
                           ".#####..#.######.###", "##...#.##########...", "#.##########.#######",
                           ".####.#.###.###.#.##", "....##.##.###..#####", ".#.#.###########.###",
                           "#.#.#.#####.####.###", "###.##.####.##.#..##"]) == (210, (11, 13))
assert vaporize([".#..##.###...#######", "##.############..##.", ".#.######.########.#",
                 ".###.#######.####.#.", "#####.##.#.##.###.##", "..#####..#.#########",
                 "####################", "#.####....###.#.#.##", "##.#################",
                 "#####.##.###..####..", "..######..##.#######", "####.##.####...##..#",
                 ".#####..#.######.###", "##...#.##########...", "#.##########.#######",
                 ".####.#.###.###.#.##", "....##.##.###..#####", ".#.#.###########.###",
                 "#.#.#.#####.####.###", "###.##.####.##.#..##"], 11, 13) == 802


def solution():
    asteroid_map = read_input_file("Files/day-10-input.txt")
    count, station = monitoring_station(asteroid_map)
    print("Part 1 ans", count)
    print("Part 2 ans", vaporize(asteroid_map, station[0], station[1]))


solution()
