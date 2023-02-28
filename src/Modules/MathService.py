import numpy
import concurrent.futures
import threading, queue 

n = 0

# ======================================================================= #
# DIVIDE AND CONQUER
# CLOSEST DISTANCE ALGORITHM

def getDistanceBetweenTwoPoints(A : numpy.array, B : numpy.array):
    global n
    n += 1
    # return numpy.linalg.norm(A - B)
    # sum of squares
    squared_sum = numpy.sum(numpy.square(A - B))
 
    # Square rooting it gives the euclidean distance
    return numpy.sqrt(squared_sum)

def AppendifNone(A, B):
    C = B[::-1]
    if (B in A) or (C in A):
        return A
    else:
        return numpy.append(A, B)

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
            allpoints = numpy.array([])
            idxmapping = numpy.array([])
            npoints = 0
            for i in range(n):
                # print(i)
                # print(i[0])
                # print(x0)
                # print(closest)
                if vectors[i][0] >= x0 - closest and vectors[i][0] <= x0 + closest:
                    allpoints = numpy.append(allpoints, vectors[i])
                    idxmapping = numpy.append(idxmapping, i)
                    npoints += 1
            allpoints = numpy.reshape(allpoints, (npoints, vectors[0].size))
            # print(allpoints)
            # print(idxmapping)
            # only need to consider these points in the slab

            # get shortest distance, compare all the points with y distance <= delta (closest) and z distance <= delta (closest) and so on for n-dimensions
            # there will always be a hard limit on the number of points for every point inside the slab, for 2D, it is 6, for 3D it is 18 and so on
            # thus O(n * n) will be O(n * k) where k is a constant, 
            # therefore O(n), even considering the pessimistic scenario where all points are in the slab
            nrow, ncol = allpoints.shape
            for i in range(0, nrow):
                for j in range(0, nrow):
                    if i != j:
                        p1 = allpoints[i]
                        p2 = allpoints[j]
                        # get all distance of p1 and p2 in the y and z dimension (in n-dimension, get all n-1 dimension's distance)
                        p3 = abs(p1 - p2)[1:]
                        # check if their distances <= delta (closest)
                        # this is the constraint (sparsity condition)
                        if all(x <= closest for x in p3):
                            distance = getDistanceBetweenTwoPoints(p1, p2)
                            if distance < closest:
                                closest = distance
                                idxpair = numpy.array([idxmapping[i], idxmapping[j]]).astype(int)
                                # print(idxpair, idxpair[0])
            
        # Calculating the T(n) : O(n log n) (from the DnC algorithm) + O(nk) (see the above comments for description) = O(n log n)
        return idxpair, numpy.round(closest, 3)








# # The same function but with threading, results : slower than the actual algorithm itself, and crashes the system if n is too high because of not enough thread
# def getClosestPairParent(vectors : numpy.array, n : int):
#         closest : float
#         idxpair = numpy.array([])
#         if (n == 1):
#             print("No Closest Pair for one point!")
#         elif (n == 2):
#             # print("Pair")
#             closest = getDistanceBetweenTwoPoints(vectors[0], vectors[1])
#             idxpair = numpy.array([0, 1])
#         elif (n == 3):
#             # print("Triplet")
#             closest = getDistanceBetweenTwoPoints(vectors[1], vectors[2])
#             idxpair = numpy.array([1, 2])
#             for i in range(0, 3):
#                 if (i != 0):
#                     temp = getDistanceBetweenTwoPoints(vectors[0], vectors[i])
#                     if temp < closest:
#                         idxpair = numpy.array([0, i])
#                         closest = temp
#         else:
#             # case 1 : smallest pair is in the same side
#             # divide the array
#             n_div = int(n / 2)
#             # print("ndiv:", n_div)

#             left = vectors[0:n_div]
#             right = vectors[n_div:n]

#             print(left)
#             print(right)
#             # print(n_div, n)

#             # split into left and right
#             Q = queue.Queue() 
#             x = threading.Thread(target=getClosestPairThread, args=(left, n_div, Q))
#             x.start()
#             y = threading.Thread(target=getClosestPairThread, args=(right, n - n_div, Q))
#             y.start()
#             x.join()
#             y.join()
#             leftidxpair, leftclosest = Q.get()
#             rightidxpair, rightclosest = Q.get()

#             # select the closest between the left and right subdivision
#             if leftclosest < rightclosest:
#                 closest = leftclosest
#                 idxpair = leftidxpair
#             elif rightclosest < leftclosest:
#                 closest = rightclosest
#                 idxpair = rightidxpair[0:rightidxpair.size] + n_div
#             else:
#                 closest = leftclosest # or right, it's the same
#                 idxpair = leftidxpair
#                 idxpair.append(rightidxpair[0:rightidxpair.size] + n_div)

#             # case 2 : smallest pair is on a separate subdivision
#             # use closest as delta
#             # x0 is the middle point of division
#             x0 = ((vectors[n_div-1][0] + vectors[n_div][0]) / 2)
#             # get all points inside the slab x0 with unbounded y and z
#             allpoints = numpy.array([])
#             idxmapping = numpy.array([])
#             for i in vectors:
#                 # print(i)
#                 # print(i[0])
#                 # print(x0)
#                 # print(closest)
#                 if i[0] >= x0 - closest and i[0] <= x0 + closest:
#                     numpy.append(allpoints, i)
#                     numpy.append(idxmapping, numpy.where(vectors == i)[0])
#             # only need to consider these points in the slab

#             # # need to take care of when dimension is 1
#             # # allpoints = allpoints.T
#             # # xprojectedallpoints = allpoints[0].T
#             # # yzprojectedallpoints = allpoints[1:allpoints.size].T
#             # # allpoints = allpoints.T

#             # get shortest distance, compare all the points with y distance <= delta (closest) and z distance <= delta (closest) and so on for n-dimensions
#             # there will always be a hard limit on the number of points for every point inside the slab, for 2D, it is 6, for 3D it is 18 and so on
#             # thus O(n * n) will be O(n * k) where k is a constant, 
#             # therefore O(n), even considering the pessimistic scenario where all points are in the slab
#             for i in range(0, allpoints.size):
#                 for j in range(0, allpoints.size):
#                     if i != j:
#                         p1 = allpoints[i]
#                         p2 = allpoints[j]
#                         # get all distance of p1 and p2 in the y and z dimension (in n-dimension, get all n-1 dimension's distance)
#                         p3 = abs(p1 - p2)[1:]
#                         # check if their distances <= delta (closest)
#                         # this is the constraint (sparsity condition)
#                         if all(x <= closest for x in p3):
#                             distance = getDistanceBetweenTwoPoints(p1, p2)
#                             if distance < closest:
#                                 closest = distance
#                                 idxpair = numpy.array([idxmapping[i], idxmapping[j]])
                            

#             # # only getting the closest on the yz-projection does not guarantee it is also the closest in 3D
#             # # mididx, midclosest = getClosestPair(yzprojectedallpoints, yzprojectedallpoints.size)
            
#         # Calculating the T(n) : O(n log n) (from the DnC algorithm) + O(nk) (see the above comments for description) = O(n log n)
#         return idxpair, numpy.round(closest, 3)

# def getClosestPairThread(vectors : numpy.array, n : int, Q):
#         closest : float
#         idxpair = numpy.array([])
#         if (n == 1):
#             print("No Closest Pair for one point!")
#         elif (n == 2):
#             # print("Pair")
#             closest = getDistanceBetweenTwoPoints(vectors[0], vectors[1])
#             idxpair = numpy.array([0, 1])
#         elif (n == 3):
#             # print("Triplet")
#             closest = getDistanceBetweenTwoPoints(vectors[1], vectors[2])
#             idxpair = numpy.array([1, 2])
#             for i in range(0, 3):
#                 if (i != 0):
#                     temp = getDistanceBetweenTwoPoints(vectors[0], vectors[i])
#                     if temp < closest:
#                         idxpair = numpy.array([0, i])
#                         closest = temp
#         else:
#             # case 1 : smallest pair is in the same side
#             # divide the array
#             n_div = int(n / 2)
#             # print("ndiv:", n_div)

#             left = vectors[0:n_div]
#             right = vectors[n_div:n]

#             print(left)
#             print(right)
#             # print(n_div, n)

#             # split into left and right
#             Q = queue.Queue() 
#             x = threading.Thread(target=getClosestPairThread, args=(left, n_div, Q))
#             x.start()
#             y = threading.Thread(target=getClosestPairThread, args=(right, n - n_div, Q))
#             y.start()
#             x.join()
#             y.join()
#             leftidxpair, leftclosest = Q.get()
#             rightidxpair, rightclosest = Q.get()

#             # select the closest between the left and right subdivision
#             if leftclosest < rightclosest:
#                 closest = leftclosest
#                 idxpair = leftidxpair
#             elif rightclosest < leftclosest:
#                 closest = rightclosest
#                 idxpair = rightidxpair[0:rightidxpair.size] + n_div
#             else:
#                 closest = leftclosest # or right, it's the same
#                 idxpair = leftidxpair
#                 idxpair.append(rightidxpair[0:rightidxpair.size] + n_div)

#             # case 2 : smallest pair is on a separate subdivision
#             # use closest as delta
#             # x0 is the middle point of division
#             x0 = ((vectors[n_div-1][0] + vectors[n_div][0]) / 2)
#             # get all points inside the slab x0 with unbounded y and z
#             allpoints = numpy.array([])
#             idxmapping = numpy.array([])
#             for i in vectors:
#                 # print(i)
#                 # print(i[0])
#                 # print(x0)
#                 # print(closest)
#                 if i[0] >= x0 - closest and i[0] <= x0 + closest:
#                     numpy.append(allpoints, i)
#                     numpy.append(idxmapping, numpy.where(vectors == i)[0])
#             # only need to consider these points in the slab

#             # # need to take care of when dimension is 1
#             # # allpoints = allpoints.T
#             # # xprojectedallpoints = allpoints[0].T
#             # # yzprojectedallpoints = allpoints[1:allpoints.size].T
#             # # allpoints = allpoints.T

#             # get shortest distance, compare all the points with y distance <= delta (closest) and z distance <= delta (closest) and so on for n-dimensions
#             # there will always be a hard limit on the number of points for every point inside the slab, for 2D, it is 6, for 3D it is 18 and so on
#             # thus O(n * n) will be O(n * k) where k is a constant, 
#             # therefore O(n), even considering the pessimistic scenario where all points are in the slab
#             for i in range(0, allpoints.size):
#                 for j in range(0, allpoints.size):
#                     if i != j:
#                         p1 = allpoints[i]
#                         p2 = allpoints[j]
#                         # get all distance of p1 and p2 in the y and z dimension (in n-dimension, get all n-1 dimension's distance)
#                         p3 = abs(p1 - p2)[1:]
#                         # check if their distances <= delta (closest)
#                         # this is the constraint (sparsity condition)
#                         if all(x <= closest for x in p3):
#                             distance = getDistanceBetweenTwoPoints(p1, p2)
#                             if distance < closest:
#                                 closest = distance
#                                 idxpair = numpy.array([idxmapping[i], idxmapping[j]])
                            

#             # # only getting the closest on the yz-projection does not guarantee it is also the closest in 3D
#             # # mididx, midclosest = getClosestPair(yzprojectedallpoints, yzprojectedallpoints.size)
            
#         # Calculating the T(n) : O(n log n) (from the DnC algorithm) + O(nk) (see the above comments for description) = O(n log n)
#         return Q.put((idxpair, numpy.round(closest, 3)))

