import re

with open('Day3/day3_example', 'r') as input:
    input = input.readlines()

pattern = r"mul\(\d+,\d+\)"
digits_pattern = r"\d+,+\d+"
dont = r"don't\(\)"
do = r'do\(\)'

do_or_dont = True

def part1():
    final_multiplications = []
    for line in input:
        matches = re.findall(pattern, line)
        for match in matches:
            match_tuple = re.findall(digits_pattern, match)
            for x in match_tuple:
                x = str(x).split(',')
                first = x[0]
                second = x[1]
                if len(first) > 3 or len(second) > 3:
                    break
                final_multiplications.append(int(first) * int(second))
    return sum(final_multiplications)

def part2():
    final_multiplications = []
    for line in input:
        matches = re.findall(pattern, line)

        for match in matches:
            match_tuple = re.findall(digits_pattern, match)
            # for x in match_tuple:
            match_tuple = str(match_tuple[0]).split(',')
            first = match_tuple[0]
            second = match_tuple[1]
            if len(first) > 3 or len(second) > 3:
                break
            if do_or_dont:
                final_multiplications.append(int(first) * int(second))
    return sum(final_multiplications)

print('Part 1: ', part1())
print('Part 2: ', part2())