fd = open('inputd3.txt', 'r')
lines = fd.read().splitlines()

for line in lines:
    print(len(line))