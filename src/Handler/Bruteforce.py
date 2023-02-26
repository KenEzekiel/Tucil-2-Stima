import math
import numpy

def bruteforce(vectors):
    # print(vectors.vecArr.shape[0])
    closest = 9999

    # VecBar = [x, y, z, ... ]
    vecBar = []

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
                print(val)
                if (val < closest):
                    closest = val
                    idxpair = [i, j]
    # TESTING
    # print(closest)
    # print(idxpair)
    
    return idxpair, numpy.round(closest, 3)
