import re

with open('Day3/day3_input', 'r') as input:
    input = input.read()

pattern = r"mul\(\d+,\d+\)"
digits_pattern = r"\d+,+\d+"
dont_or_do = r"don't\(\)(.*)do\(\)"
dont_do_it = r"don't(.*)"

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
    remove_dont = re.search(dont_or_do, input).group()
    # for dont in remove_dont:
    new_input = input.replace(remove_dont, "")
    matches = re.findall(pattern, new_input)
    dont_at_end = re.match(dont_do_it, new_input)
    if dont_at_end:
        new_input.replace(dont_at_end, new_input)
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