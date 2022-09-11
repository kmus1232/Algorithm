setdata = ['A', 'B', 'C', 'D']

def printSubsets(arr):
    n = len(arr)
    for i in range(1 << n):
        print('{', end=' ')
        for j in range(n):
            if i & (1 << j):
                print(arr[j], end=' ')
        print('}')

printSubsets(setdata)