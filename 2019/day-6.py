# Problem Statement
# https://adventofcode.com/2019/day/6


def read_input_file(file):
    with open(file) as file:
        return file.readlines()


def path(orbiter, graph):
    return [graph.get(orbiter)] + path(graph.get(orbiter), graph) if graph.get(orbiter) else []


def create_graph(space_map):
    return {orbiter: center for center, orbiter in [item.strip().split(")") for item in space_map]}


def total_orbits(space_map):
    graph = create_graph(space_map)
    return sum([len(path(orbiter, graph)) for orbiter in graph])


def transfers(space_map):
    orbit_map = create_graph(space_map)
    santa_path = path("SAN", orbit_map)
    you_path = path("YOU", orbit_map)

    for index, parent in enumerate(you_path):
        if parent in santa_path:
            return index + santa_path.index(parent)


# Unit tests
assert total_orbits(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']) == 42
assert transfers(['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']) == 4


def solution():
    print("Part 1 ans", total_orbits(read_input_file("Files/day-6-input.txt")))
    print("Part 2 ans", transfers(read_input_file("Files/day-6-input.txt")))


solution()
