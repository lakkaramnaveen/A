arr = [1, 12, 42, 21, 34, 21]
arr.sort()

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


if __name__ == '__main__':
    print(binarySearch(arr, 13))
    print(linearSearch(arr, 12))
    print(recursiveBinarySearch(arr, 12322, 0, len(arr)-1))
