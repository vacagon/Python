import re

file = open('regex_sum_1649624.txt')
numList = list()
for line in file:
    line = line.split()
    for word in line:
        num_string = re.findall('[0-9]+', word)
        if len(num_string) != 1: continue
        print(num_string)
        num = float(num_string[0])
        numList.append(num)
print(sum(numList))
