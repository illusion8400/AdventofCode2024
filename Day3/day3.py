import re

with open('Day3/day3_input', 'r') as input:
    input = input.readlines()

pattern = r"mul\(\d+,\d+\)"
digits_pattern = r"\d+,+\d+"
final_multiplications = []

def part1():
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
    print('Part 1: ', sum(final_multiplications))

part1()