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

def incCount(count):
    count += 1
    if (count == 2):
        count = incCount(count)
    return count

test = 1
test = incCount(test)
print(test)