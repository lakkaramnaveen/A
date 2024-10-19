han = open('A.txt')

# print(dir(han))

for line in han:
    print(line)
    line = line.strip()
    wds = line.split()
    # print(wds)
    try:
        if wds[0] == 'help':
            continue
        else:
            print(wds[1])
    except:
        print('empty')
    finally:
        print('nani')
