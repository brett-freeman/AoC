fd = open('sample_input', 'r')
lines = fd.read().splitlines()

symbols = [
    '*',
    '#',
    '$',
    '+'
]

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c.isdigit():
            print(lines[i-1], lines[i+1])
