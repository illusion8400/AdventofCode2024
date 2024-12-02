with open("Day2/day2_example") as input:
    input = input.readlines()

count = 0
safe = []
unsafe = []
for report in input:
    report = report.split()
    if all(report[i] <= report[i + 1] for i in range(len(report) - 1)):
        #
        for level in range(len(report) - 1):
            cur_level = report[level]
            next_level = report[level + 1]
            if int(max(cur_level, next_level)) - int(min(cur_level, next_level)) > 3:
                break
        else:
            count += 1
            
    elif all(report[i] >= report[i + 1] for i in range(len(report) - 1)):
        #
        for level in range(len(report) - 1):
            cur_level = report[level]
            next_level = report[level + 1]
            if int(max(cur_level, next_level)) - int(min(cur_level, next_level)) > 3:
                break
        else:
            count += 1
            
    else:
        continue
print(count)