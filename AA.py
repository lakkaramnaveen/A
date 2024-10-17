expenses = [{"January":2200}, {"February":2500},{"March":2600},{"April":2130},{"May":2190}]

expenses.append({"June":1980})
# for i in range(0,3):

print(expenses)


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
