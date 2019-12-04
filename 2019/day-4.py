# Problem Statement
# https://adventofcode.com/2019/day/4


def valid_passwords_in_range(start, end):
    passwords = []
    for password in range(start, end + 1):
        if valid(password):
            passwords.append(password)
    return passwords


def valid(password):
    return non_decreasing(password) and duplicate(password)


def non_decreasing(number):
    prev = 0
    num_str = str(number)
    for digit in num_str:
        if prev > int(digit):
            return False
        prev = int(digit)
    return True


def duplicate(number):
    prev = 0
    num_str = str(number)
    for digit in num_str:
        if prev == int(digit):
            return True
        prev = int(digit)
    return False


def strict_duplicate(number):
    count = {}
    num_str = str(number)
    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i + 1]:
            count[num_str[i]] = count.get(num_str[i], 1) + 1

    return True if 2 in count.values() else False


# Unit tests
assert non_decreasing(111111)
assert not non_decreasing(123435)
assert duplicate(122456)
assert valid(111111)
assert not valid(223450)
assert not valid(123789)
assert strict_duplicate(112233)
assert not strict_duplicate(123444)
assert strict_duplicate(111122)


def solution(start, end):
    passwords = valid_passwords_in_range(start, end)
    part2 = [password for password in passwords if strict_duplicate(password)]
    print("Part 1 ans", len(passwords))
    print("Part 2 ans", len(part2))


solution(359282, 820401)
