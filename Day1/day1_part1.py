with open("Day1/day1_input", "r") as input:
    input = input.readlines()

column_a = []
column_b = []
column_differences = []
for line in input:
    column_a.append(line.split()[0])
    column_b.append(line.split()[1])
count = len(column_a)
for x in range(0, count):
    min_set = [min(column_a), min(column_b)]
    if min_set[0] == min_set[1]:
        column_differences.append(0)
        column_a.pop(column_a.index(min_set[0]))
        column_b.pop(column_b.index(min_set[1]))
    elif min_set[0] >= min_set[1]:
        column_differences.append(int(min_set[0]) - int(min_set[1]))
        column_a.pop(column_a.index(min_set[0]))
        column_b.pop(column_b.index(min_set[1]))
        # print("")
    else:
        column_differences.append(int(min_set[1]) - int(min_set[0]))
        column_a.pop(column_a.index(min_set[0]))
        column_b.pop(column_b.index(min_set[1]))
        # print("")
# print(column_a, column_b)
# print(column_differences)
print(sum(column_differences))