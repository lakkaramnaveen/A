searchNumber = int(input('Enter any number to search: '))
arrayInt = [1, 11, 12, 14, 5, 6, 23, 4, 87]
arrayInt.sort()


def binarySearch(arrayInt, searchNumber):
    f = False
    low = 0
    high = len(arrayInt)-1
    while(low<=high):
        mid = int((low + high) / 2)
        if arrayInt[mid] == searchNumber:
            return True
        elif arrayInt[mid] < searchNumber:
            low = mid + 1
        else:
            high = mid - 1
    return f


print(binarySearch(arrayInt,searchNumber))
