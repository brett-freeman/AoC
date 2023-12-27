fd = open('d1input', 'r')
lines = fd.read().splitlines()
ans = 0
wordnum = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

for line in lines:
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for j, num in enumerate(wordnum):
            if line[i:i+len(num)] == num:
                digits.append(str(j+1))
    ans += int(digits[0] + digits[-1])
print(ans)
