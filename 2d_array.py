from array import *

N = 5
array = [5]*N
print(array)
print(" ")

A = [[10, 15, 1, 9], [19, 4, 11], [17, 9, 12, 0], [12, 11, 8, 5]]
print(A[0])
print(A[1][2])
print(" ")

A[3] = [11, 4, 1]
A[0][3] = 8
del A[1]
A.insert(3, [7, 3, 17, 18])


for e in A:
    for s in e:
        print(s, end = " ")
    print()
