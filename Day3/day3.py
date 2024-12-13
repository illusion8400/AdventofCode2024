import re

with open('Day3/day3_input', 'r') as input:
    input = input.read()

pattern = re.compile(r"mul\(\d+,\d+\)")
digits_pattern = re.compile(r"\d+,+\d+")
dont_or_do = r"don't\(\)+(.*)do\(\)+"
dont_do_it = re.compile(r"don't(.*)")

def part1():
    final_multiplications = []
    matches = re.findall(pattern, input)
    for match in matches:
        match_tuple = re.findall(digits_pattern, match)
        for x in match_tuple:
            x = str(x).split(',')
            first = x[0]
            second = x[1]
            if len(first) > 3 or len(second) > 3:
                continue
            final_multiplications.append(int(first) * int(second))
    return sum(final_multiplications)

def part2():
    final_multiplications = []
    remove_dont = re.findall(dont_or_do, input.strip())
    for dont in remove_dont:
        new_input = input.replace(dont, "")
    matches = re.findall(pattern, new_input.strip())
    for match in matches:
        match_tuple = re.findall(digits_pattern, match)
        # for x in match_tuple:
        match_tuple = str(match_tuple[0]).split(',')
        first = match_tuple[0]
        second = match_tuple[1]
        if len(first) > 3 or len(second) > 3:
            continue

        final_multiplications.append(int(first) * int(second))
    return sum(final_multiplications)

print('Part 1: ', part1())
print('Part 2: ', part2())