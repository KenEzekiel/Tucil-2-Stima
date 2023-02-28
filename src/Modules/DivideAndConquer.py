import numpy
import math

n = 0
showProgress = False

# ======================================================================= #
# DIVIDE AND CONQUER
# CLOSEST DISTANCE ALGORITHM

def getDistanceBetweenTwoPoints(A : numpy.array, B : numpy.array):
    global n
    global showProgress
    # Show progress
    if showProgress and n % 1000 == 0:
        print(f"[{n+1} operations completed]")
    n += 1
    # return numpy.linalg.norm(A - B)
    # sum of squares
    squared_sum = numpy.sum(numpy.square(A - B))
 
    # Square rooting it gives the euclidean distance
    return numpy.sqrt(squared_sum)


def getClosestPair(vectors : numpy.array, n : int):
        closest : float
        idxpair = numpy.array([])
        if (n == 1):
            # print("No Closest Pair for one point!")
            pass
        elif (n == 2):
            # print("Pair")
            closest = getDistanceBetweenTwoPoints(vectors[0], vectors[1])
            idxpair = numpy.array([0, 1])
        elif (n == 3):
            # print("Triplet")
            closest = getDistanceBetweenTwoPoints(vectors[1], vectors[2])
            idxpair = numpy.array([1, 2])
            for i in range(0, 3):
                if (i != 0):
                    temp = getDistanceBetweenTwoPoints(vectors[0], vectors[i])
                    if temp < closest:
                        idxpair = numpy.array([0, i])
                        closest = temp
        else:
            # case 1 : smallest pair is in the same side
            # divide the array
            n_div = int(n / 2)
            # print("ndiv:", n_div)

            left = vectors[0:n_div]
            right = vectors[n_div:n]

            # print(left)
            # print(right)
            # print(n_div, n)

            # split into left and right
            leftidxpair, leftclosest = getClosestPair(left, n_div)
            rightidxpair, rightclosest = getClosestPair(right, n - n_div)

            # select the closest between the left and right subdivision
            if leftclosest < rightclosest:
                closest = leftclosest
                idxpair = leftidxpair
            elif rightclosest < leftclosest:
                closest = rightclosest
                idxpair = rightidxpair[0:rightidxpair.size] + n_div
            else:
                closest = leftclosest # or right, it's the same
                idxpair = numpy.append(leftidxpair, rightidxpair[0:rightidxpair.size] + n_div)

            # case 2 : smallest pair is on a separate subdivision
            # use closest as delta
            # x0 is the middle point of division
            x0 = ((vectors[n_div-1][0] + vectors[n_div][0]) / 2)
            # get all points inside the slab x0 with unbounded y and z
            allpointsleft = numpy.array([])
            allpointsright = numpy.array([])
            idxmappingleft = numpy.array([])
            idxmappingright = numpy.array([])
            npointsleft = 0
            npointsright = 0
            for i in range(n):
                # print(i)
                # print(i[0])
                # print(x0)
                # print(closest)
                if vectors[i][0] >= x0 - closest and vectors[i][0] < x0:
                    allpointsleft = numpy.append(allpointsleft, vectors[i])
                    idxmappingleft = numpy.append(idxmappingleft, i)
                    npointsleft += 1
                if vectors[i][0] >= x0 and vectors[i][0] <= x0 + closest: # points in the middle included in the right, if there is (should be none)
                    allpointsright = numpy.append(allpointsright, vectors[i])
                    idxmappingright = numpy.append(idxmappingright, i)
                    npointsright += 1
            allpointsleft = numpy.reshape(allpointsleft, (npointsleft, vectors[0].size))
            allpointsright = numpy.reshape(allpointsright, (npointsright, vectors[0].size))
            # print(allpointsleft, allpointsright)
            # print(idxmapping)
            # only need to consider these points in the slab

            # get shortest distance, compare all the points with y distance <= delta (closest) and z distance <= delta (closest) and so on for n-dimensions
            # there will always be a hard limit on the number of points for every point inside the slab, for 2D, it is 6, for 3D it is 18 and so on
            # thus O(n * n) will be O(n * k) where k is a constant, 
            # therefore O(n) for every dimension except x thus O(n*(k^(d-1))), even considering the pessimistic scenario where all points are in the slab
            nrowleft, ncolleft = allpointsleft.shape
            nrowright, ncolright = allpointsright.shape
            for i in range(0, nrowleft):
                for j in range(0, nrowright):
                        p1 = allpointsleft[i]
                        p2 = allpointsright[j]
                        # get all distance of p1 and p2 in the y and z dimension (in n-dimension, get all n-1 dimension's distance)
                        p3 = abs(p1 - p2)[1:]
                        # check if their distances <= delta (closest)
                        # this is the constraint (sparsity condition)
                        if all(x <= closest for x in p3):
                            distance = getDistanceBetweenTwoPoints(p1, p2)
                            if distance < closest:
                                closest = distance
                                idxpair = numpy.array([idxmappingleft[i], idxmappingright[j]]).astype(int)
                                # print(idxpair, idxpair[0])
            
        # Calculating the T(n) : O((n*(k^(d - 1)))log n) = O(n log n) (from the DnC algorithm) (where d is the dimension and k is a constant) (see the above comments for description)
        return idxpair, numpy.round(closest, 3)

