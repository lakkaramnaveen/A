def bubble_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    elements = [5,4,5,12,3,1,24,56,77,86,3,783,32]
    bubble_sort(elements)
    print(elements)
