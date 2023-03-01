import math
import numpy

n = 0
showProgress = False

def bruteforce(vectors: numpy.array):
    global n
    global showProgress
    # print(vectors.vecArr.shape[0])
    closest = (numpy.sqrt(numpy.sum(numpy.square(vectors[1][:] - vectors[0][:]))))

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

                # Show progrss
                # if showProgress:
                #     print(f"[{n % (int(((vectors.shape[0]-1)**2)*(0.1)))}")
                if showProgress:
                    if ((vectors.shape[0]-1)**2) < 10:
                        print(f"[{n+1} / {(vectors.shape[0]-1)**2}] operations")
                    elif ((n % int(((vectors.shape[0]-1)**2)*(0.1)) == 0)):
                        print(f"[{n+1} / {(vectors.shape[0]-1)**2}] operations")
                n += 1

                # Checking
                if (val < closest):
                    closest = val
                    idxpair = numpy.array([i, j])
                elif (val == closest) and ([j, i] not in idxpair):
                    idxpair = numpy.append(idxpair, [i, j])
                
    # TESTING
    # print(closest)
    # print(idxpair)

    return idxpair, numpy.round(closest, 3)
