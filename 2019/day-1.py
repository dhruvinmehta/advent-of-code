# Problem Statement
# https://adventofcode.com/2019/day/1


def read_input_file(file):
    with open(file) as file:
        return [int(module.strip()) for module in file]


def fuel_for_mass(mass):
    return int(mass / 3) - 2


def fuel_for_complete_load(fuel):
    total_fuel = 0
    while fuel > 0:
        fuel = fuel_for_mass(fuel)
        if fuel > 0:
            total_fuel += fuel
    return total_fuel


# Unit tests
assert fuel_for_mass(12) == 2
assert fuel_for_mass(14) == 2
assert fuel_for_mass(1969) == 654
assert fuel_for_mass(100756) == 33583
assert fuel_for_complete_load(1969) == 966
assert fuel_for_complete_load(100756) == 50346


def solution():
    modules = read_input_file("Files/day-1-input.txt")

    fuel_to_load = 0
    total_fuel = 0
    for mass in modules:
        fuel_to_load += fuel_for_mass(mass)
        total_fuel += fuel_for_complete_load(mass)
    print("Part 1 ans", fuel_to_load)
    print("Part 2 ans", total_fuel)


solution()
