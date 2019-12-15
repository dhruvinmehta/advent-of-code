# Problem Statement
# https://adventofcode.com/2019/day/14

import math

ORE_STOCK = 1000000000000


def read_input_file(file):
    with open(file) as file:
        return [line for line in file.readlines()]


def parse(reaction_input):
    reactions = {}
    for reaction in reaction_input:
        source, output = reaction.split("=>")
        source_map = {}
        for s in source.split(","):
            quantity, fuel = s.strip().split(" ")
            source_map[fuel] = int(quantity)
        quantity, fuel = output.strip().split(" ")
        reactions[fuel] = int(quantity), source_map
    return reactions


def next_fuel(required):
    for fuel in required:
        if required[fuel] > 0 and fuel != 'ORE':
            return fuel


def required_raw_fuel(reaction_input, req_quantity):
    reactions = parse(reaction_input)
    required = {'FUEL': req_quantity}
    while any(required[fuel] > 0 and fuel != 'ORE' for fuel in required):
        fuel = next_fuel(required)
        generated_quantity, sources = reactions[fuel]
        units = math.ceil(required[fuel] / generated_quantity)
        required[fuel] -= generated_quantity * units

        for fuel in sources:
            required[fuel] = required.get(fuel, 0) + sources[fuel] * units
    return required['ORE']


def generate_fuel(reaction_input):
    low = 0
    high = ORE_STOCK * 2

    while low < high:
        mid = (low + high + 1) // 2
        raw_fuel = required_raw_fuel(reaction_input, mid)
        if raw_fuel > ORE_STOCK:
            high = mid - 1
        elif raw_fuel < ORE_STOCK:
            low = mid
    return low


# Unit tests
assert parse(["7 A, 1 B => 1 C"]) == {'C': (1, {'A': 7, 'B': 1})}
assert required_raw_fuel(["10 ORE => 10 A", "1 ORE => 1 B", "7 A, 1 B => 1 C", "7 A, 1 C => 1 D",
                          "7 A, 1 D => 1 E", "7 A, 1 E => 1 FUEL"], 1) == 31
assert required_raw_fuel(["9 ORE => 2 A", "8 ORE => 3 B", "7 ORE => 5 C", "3 A, 4 B => 1 AB", "5 B, 7 C => 1 BC",
                          "4 C, 1 A => 1 CA", "2 AB, 3 BC, 4 CA => 1 FUEL"], 1) == 165
assert required_raw_fuel(["157 ORE => 5 NZVS", "165 ORE => 6 DCFZ",
                          "44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL",
                          "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ", "179 ORE => 7 PSHF", "177 ORE => 5 HKGWZ",
                          "7 DCFZ, 7 PSHF => 2 XJWVT", "165 ORE => 2 GPVTF",
                          "3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"], 1) == 13312
assert generate_fuel(["157 ORE => 5 NZVS", "165 ORE => 6 DCFZ",
                      "44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL",
                      "12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ", "179 ORE => 7 PSHF", "177 ORE => 5 HKGWZ",
                      "7 DCFZ, 7 PSHF => 2 XJWVT", "165 ORE => 2 GPVTF",
                      "3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"]) == 82892753


def solution():
    print("Part 1 ans", required_raw_fuel(read_input_file("Files/day-14-input.txt"), 1))
    print("Part 2 ans", generate_fuel(read_input_file("Files/day-14-input.txt")))


solution()
