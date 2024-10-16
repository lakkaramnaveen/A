def squaree(numbers):
    squared = []
    for n  in numbers:
        squared.append(n * n)
    return squared

n = [1,4,2,6,3]
print(squaree(n))
