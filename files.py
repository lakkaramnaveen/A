han = open('A.txt')
for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1 or wds[0] != 'help':
        continue
    else:
        print(wds[1])

garage = dict()

garage['car'] = 'AUDI'
print(dir(garage))
