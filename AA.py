exp = [2200,2350,2600,2130,2190]

print(exp[1] - exp[0])
print(exp[0]+exp[1]+exp[2])
print("Did I spent 2000$ in any month? ", 2000 in exp)
exp.append(1980)
print(exp)
exp[3] = exp[3] - 200
print(exp)

# 2:

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))

heros.append("black panther")
print(heros)

heros.remove("black panther")
print(heros)

heros.insert(2,"black")
print(heros)

heros[1] = heros[2] = 'doctor strange'
print(heros)

heros.sort()
print(heros)


# 3:
# l = []
# maxNumber = int(input('What is the number: '))
# for i in range(1,maxNumber):
#     if i%2!=0:
#         l.append(i)

# print("Odd numbers: ", l)
