fd = open('d1input', 'r')
lines = fd.read().splitlines()
ans = 0

for line in lines:
    digits = []
    for c in line:
        if c.isdigit():
            digits.append(c)
    ans += int(digits[0] + digits[-1])

print(ans)
