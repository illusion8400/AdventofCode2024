with open("Day1/day1_input", "r") as input:
    input = input.readlines()

column_a = []
column_b = []
column_similarities = []
for line in input:
    column_a.append(line.split()[0])
    column_b.append(line.split()[1])
count = len(column_a)
for x in column_a:
    count = 0
    for y in column_b:
        if x == y:
            count += 1
    else:
        column_similarities.append(int(x) * count)

print(sum(column_similarities))