fd = open('d2input', 'r')
lines = fd.read().splitlines()

ans = 0

for i, game in enumerate(lines):
    max = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for round in game.split(': ')[1].split('; '):
        for roll in round.split(', '):
            if int(roll.split(' ')[0]) > max[roll.split(' ')[1]]:
                max[roll.split(' ')[1]] = int(roll.split(' ')[0])
    ans += int(max['red'] * max['green'] * max['blue'])
print(ans)
