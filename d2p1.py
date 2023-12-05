import re

red_max = 12
green_max = 13
blue_max = 14

output = 0

fd = open('inputd2.txt', 'r')
lines = fd.read().splitlines()

for line in lines:
    red_fail = False
    green_fail = False
    blue_fail = False

    id = line.split(':')[0].split(' ')[1]

    red = re.findall(r'(\d+)\s+red', line)
    green = re.findall(r'(\d+)\s+green', line)
    blue = re.findall(r'(\d+)\s+blue', line)

    for i in red:
        if int(i) > red_max:
            red_fail = True
    for i in green:
        if int(i) > green_max:
            green_fail = True
    for i in blue:
        if int(i) > blue_max:
            blue_fail = True
    if not red_fail and not green_fail and not blue_fail:
        output += int(id)

print(output)