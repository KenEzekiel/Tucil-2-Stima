import math
import numpy

n = 0

def bruteforce(vectors):
    global n
    # print(vectors.vecArr.shape[0])
    closest = 9999

    # VecBar = [x, y, z, ... ]
    vecBar = []
    idxpair = numpy.array([])

    for i in range(0, vectors.shape[0]):
        for j in range(1, vectors.shape[0]):

            # Iterate according to dimentions
            if (i != j):
                for k in range(0, vectors.shape[1]):
                    temp = 0
                    vecBar.append(vectors[j][k] - vectors[i][k])
                    for p in range(len(vecBar)):
                        temp += pow(vecBar[p],2)

                    # TESTING
                    # print(vecBar)
                vecBar = []

                # Check if value is smaller than closest value
                val = math.sqrt(temp)

                # TESTING
                # print(val)
                n += 1
                if (val < closest):
                    closest = val
                    idxpair = numpy.array([i, j])
    # TESTING
    # print(closest)
    # print(idxpair)

    return idxpair, numpy.round(closest, 3)
