with open("Day1/day1_input", "r") as input:
    input = input.readlines()

column_a = []
column_b = []
column_differences = []
column_similarities = []

for line in input:
    column_a.append(line.split()[0])
    column_b.append(line.split()[1])

def pop_columns(min_set):
    column_a.pop(column_a.index(min_set[0]))
    column_b.pop(column_b.index(min_set[1]))

def part_1():
    count = len(column_a)
    for _ in range(0, count):
        min_set = [min(column_a), min(column_b)]
        if min_set[0] == min_set[1]:
            column_differences.append(0)
            pop_columns(min_set)
        elif min_set[0] >= min_set[1]:
            column_differences.append(int(min_set[0]) - int(min_set[1]))
            pop_columns(min_set)
        else:
            column_differences.append(int(min_set[1]) - int(min_set[0]))
            pop_columns(min_set)

    return sum(column_differences)

def part_2():
    for line in input:
        column_a.append(line.split()[0])
        column_b.append(line.split()[1])
    for x in column_a:
        count = 0
        for y in column_b:
            if x == y:
                count += 1
        else:
            column_similarities.append(int(x) * count)

    return sum(column_similarities)


print(f"Part 1: {part_1()}\nPart 2: {part_2()}")