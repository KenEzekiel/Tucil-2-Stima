import numpy as np
import MathService

# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]])
# A = A.T
# A = A[1:A.size]
# A = A.T
# A = np.array([(1,2)], dtype=object)
# print(A)
# # print(np.append(A, [[1, 2]], axis=0))
# print(MathService.AppendifNone(A, (4,5)))

# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [1, 2, 4]
# ])
# print(A)
# for i in A:
#     for j in A:
#         if not np.array_equal(i, j):
#             print(i, j)

# p1 = np.array([1,2,3])
# p2 = np.array([5,5,5])
# p3 = abs(p1 - p2)[1:]
# print(all(i < 3 for i in p3))

# print(p3)

# def incCount(count):
#     count += 1
#     if (count == 2):
#         count = incCount(count)
#     return count

# test = 1
# test = incCount(test)
# print(test)

# a = np.array([768.929,  89.633, 665.532, 131.119])
# b = np.array([768.932, 100.412, 618.973, 101.508])

a = np.array([1, 2, 3])
b = np.array([9, 5, 6])

c = np.array([904.723, 643.611, 751.382, 546.22])
d = np.array([913.948, 622.687, 747.749, 538.427])

p3 = abs(a - b)[1:]

if all(x <= 3 for x in p3):
    distance = MathService.getDistanceBetweenTwoPoints(a, b)
    print(distance)

# print(MathService.getDistanceBetweenTwoPoints(a, b))
# print(MathService.getDistanceBetweenTwoPoints(c, d))
