arr = [1, 12, 42, 21, 34, 21]
arr.sort()

class Nani:
    def binarySearch(self, a, element):
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

    def linearSearch(self, a, element):
        for i in a:
            if i == element:
                return True
        return False


if __name__ == '__main__':
    bin = Nani()
    print(bin.binarySearch(arr, 13))
    print(bin.linearSearch(arr, 12))
