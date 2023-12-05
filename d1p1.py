import re

fd = open('inputd1.txt', 'r')
lines = fd.readlines()

output = 0

for line in lines:
    line = re.sub('[^\d]', '', line)
    cv = line[0] + line[-1]
    output += int(cv)
        
print(output)