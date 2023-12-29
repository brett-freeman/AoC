fd = open('sample_input', 'r')
lines = fd.read().splitlines()

partnums = []

match_symbols = [
    '*',
    '+',
    '$',
    '#'
]

numbers = {}
symbols = {}

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '.':
            pass
        elif c.isdigit():
            numbers[(i, j)] = int(c)
        else:
            symbols[(i, j)] = c
for i, (coord_sym, symbol) in enumerate(symbols.items()):
    for j, (coord_num, num) in enumerate(numbers.items()):
        if coord_sym[0] == coord_num[0]:
            print('same line')
