with open("Day2/day2_input") as input:
    input = input.readlines()

count = 0
safe = []
unsafe = []
for report in input:
    count += 1
    report = report.split()
    if all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or all(report[i] >= report[i + 1] for i in range(len(report) - 1)):
        #
        for level in range(len(report) - 1):
            cur_level = report[level]
            next_level = report[level + 1]
            if int(abs(int(cur_level) - int(next_level))) > 3 or cur_level == next_level:
                unsafe.append(report)
                break
        else:
            safe.append(report)

    else:
        unsafe.append(report)
        
print("unsafe")
# print(unsafe)
print(len(unsafe))
# print(safe)
print("safe")
print(len(safe))