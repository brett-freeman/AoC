fd = open('inputd1.txt', 'r')
lines = fd.read().splitlines()
output = 0

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

for line in lines:
    i = 0
    x = 0
    firstdigit = 0
    lastdigit = 0

    while i < 1:
        if line[0].isdigit():
            firstdigit = line[0]
            i = 1
        elif line[:3] in digits:
            firstdigit = digits[line[:3]]
            i = 1
        elif line[:4] in digits:
            firstdigit = digits[line[:4]]
            i = 1
        elif line[:5] in digits:
            firstdigit = digits[line[:5]]
            i = 1
        else:
            line = line[1:]

    while x < 1:
        if line[-1].isdigit():
            lastdigit = line[-1]
            x = 1
        elif line[-3:] in digits:
            lastdigit = digits[line[-3:]]
            x = 1
        elif line[-4:] in digits:
            lastdigit = digits[line[-4:]]
            x = 1
        elif line[-5:] in digits:
            lastdigit = digits[line[-5:]]
            x = 1
        else:
            line = line[:-1]
    
    cv = firstdigit + lastdigit
    output += int(cv)
print(output)