import numpy

# ======================================================================= # 

# DIVIDE AND CONQUER
# QUICK SORT

def partitioning(vectors: numpy.array, dimension:int, lowerBound: int, upperBound: int):
    # Choose the pivoting
    pivot = vectors[0][upperBound]
    # Pointer
    i = lowerBound - 1

    # Traverse and comparing value with pivot
    for j in range(lowerBound, upperBound):
        # Swapping if value is lower
        if vectors[0][j] <= pivot:
            i += 1
            for k in range(dimension):
                (vectors[k][i], vectors[k][j]) = (vectors[k][j], vectors[k][i])
    # Swapping pivot element
    for p in range(dimension):
        (vectors[p][i+1], vectors[p][upperBound]) = (vectors[p][upperBound], vectors[p][i+1])
    # Return pointer
    return (i+1)

def quickSort(vectors: numpy.array, dimension: int, lowerBound: int, upperBound: int):
    if lowerBound < upperBound:
        # Finding pivot element
        x = partitioning(vectors, dimension, lowerBound, upperBound)
        # Recursive on the left and right of pivot
        quickSort(vectors, dimension, lowerBound, x-1)
        quickSort(vectors, dimension, x+1, upperBound)

