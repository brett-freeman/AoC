import re

output = 0

fd = open('inputd2.txt', 'r')
lines = fd.read().splitlines()
output = 0

for line in lines:
    red = re.findall(r'(\d+)\s+red', line)
    green = re.findall(r'(\d+)\s+green', line)
    blue = re.findall(r'(\d+)\s+blue', line)

    red_min = 0
    green_min = 0
    blue_min = 0

    for i in red:
        if int(red_min) < int(i):
            red_min = i
    for i in green:
        if int(green_min) < int(i):
            green_min = i
    for i in blue:
        if int(blue_min) < int(i):
            blue_min = i   
    power = int(red_min) * int(green_min) * int(blue_min)
    output += power
print(output)