fd = open('d2input', 'r')
lines = fd.read().splitlines()

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}
ans = 0

for i, game in enumerate(lines):
    failed = False
    for round in game.split(': ')[1].split('; '):
        for roll in round.split(', '):
            if int(roll.split(' ')[0]) > limits[roll.split(' ')[1]]:
                failed = True
    if not failed:
        ans += i+1
print(ans)
