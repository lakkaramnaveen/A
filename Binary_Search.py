def binarySearch(a, element):
    mid = low = 0
    high = len(a)
    while(low<=high):
        mid = int( (low + high)/2 )
        if arr[mid] == element:
            return True
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return False

def recursiveBinarySearch(a, element, low, high):
    if high < low:
        return -1
    mid = (low + high)//2
    if arr[mid] == element:
        return mid
    elif arr[mid] < element:
        low = mid + 1
    else:
        high = mid - 1
    return recursiveBinarySearch(a, element, low, high)

def linearSearch(a, element):
    for i in a:
        if i == element:
            return True
    return False

def allOccurences(a, element):
    list1 = []
    for i in range(len(a)-1):
        if a[i] == element:
            list1.append(i)
    return list1

if __name__ == '__main__':
    arr = [1, 12, 42, 21, 34, 21]
    numbers = [1,4,6,9,10,5,7]
    # numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    numbers.sort()
    print(binarySearch(numbers, 5))
    print(linearSearch(numbers, 5))
    print(recursiveBinarySearch(numbers, 5, 0, len(numbers)-1))
    print(allOccurences(numbers, 10))
