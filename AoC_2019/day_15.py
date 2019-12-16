# Problem Statement
# https://adventofcode.com/2019/day/15

import copy
from AoC_2019.Common.Computer import Computer


def read_input_file(file):
    with open(file) as file:
        return [int(element) for element in file.read().split(",")]


DIRECTION = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}


def find_shortest_path(instructions):
    area_map = create_area_map(instructions)
    graph = create_graph(area_map)
    visited = set()
    queue = [(0, 0)]
    level = {(0, 0): 0}

    while queue:
        node = queue.pop(0)
        for neighbour in graph[node]:
            if neighbour not in visited:
                level[neighbour] = level[node] + 1
                if area_map[neighbour] == 'O':
                    return level[neighbour]
                queue.append(neighbour)
        visited.add(node)


def create_area_map(instructions):
    queue = [(0, 0)]
    tile = ['#', '.', 'O']
    area_map = {(0, 0): '.'}
    visited = {(0, 0): Computer(instructions, True)}
    while queue:
        x, y = queue.pop(0)
        for move in DIRECTION:
            new_x, new_y = x + DIRECTION[move][0], y + DIRECTION[move][1]
            if (new_x, new_y) not in visited:
                computer = copy.deepcopy(visited[(x, y)])
                computer.set_input(move)
                output = computer.execute()
                area_map[(new_x, new_y)] = tile[output]
                visited[(new_x, new_y)] = computer
                if output != 0:
                    queue.append((new_x, new_y))
    return area_map


def create_graph(area_map):
    graph = {}
    for (x, y) in area_map:
        if area_map[(x, y)] != '#':
            for dx, dy in DIRECTION.values():
                if (x + dx, y + dy) in area_map and area_map[(x + dx, y + dy)] != '#':
                    if (x, y) in graph:
                        graph[(x, y)].append((x + dx, y + dy))
                    else:
                        graph[(x, y)] = [(x + dx, y + dy)]
    return graph


def fill_oxygen(instructions):
    area_map = create_area_map(instructions)
    queue = [point for point in area_map if area_map[point] == 'O']
    length = len(queue)
    visited = set()
    minutes = -1
    while queue:
        children = 0
        for _ in range(length):
            x, y = queue.pop(0)
            for dx, dy in DIRECTION.values():
                if (x + dx, y + dy) not in visited and area_map[(x + dx, y + dy)] == '.':
                    queue.append((x + dx, y + dy))
                    children += 1
            visited.add((x, y))
        length = children
        minutes += 1
    return minutes


def solution():
    print("Part 1 ans", find_shortest_path(read_input_file("Files/day-15-input.txt")))
    print("Part 2 ans", fill_oxygen(read_input_file("Files/day-15-input.txt")))


solution()
