# Importing Libraries
from Modules.Sorting import partitioning
from Modules.Sorting import quickSort

import numpy
from numpy.random import Generator, PCG64
import time

class InputHandler():
    def __init__(self, num: int, dimension: int, size: int, decimalOn=True, randomize=True, inputVector=numpy.array([])):
        self.num = num
        self.dimension = dimension
        self.size = size
        self.vecArr = []

        # option to randomize the vectors or not
        if (randomize):
            self.randomizeVector()
        else:
            self.vecArr = inputVector
        # option to use decimals or not
        if not decimalOn:
            self.vecArr = numpy.round(self.vecArr)
        else:
            self.vecArr = numpy.round(self.vecArr, 3)

        # Preprocessing
        # Sorting Array
        self.vecArr = numpy.transpose(self.vecArr)
        quickSort(self.vecArr, 0, self.num-1)
        self.vecArr = numpy.transpose(self.vecArr)
        # print(self.vecArr)
    
    def randomizeVector(self):
        print("Randomizing vectors...")
        
        # self.vecArr = numpy.random.uniform(low=0.0, high=self.size, size=(self.num, self.dimension))
        vector = []
        for i in range(self.num * self.dimension):
            a = numpy.random.uniform(low=0.0, high=self.size)
            vector.append(a)
    
        # print(vector)
        self.vecArr = numpy.array(vector).reshape(self.num, self.dimension)
        # print("sizze: ")
        # print(self.size)
        # print("vector: ")
        # print(self.vecArr)
        
        # self.vecArr = self.size * self.vecArr

    def printVectors(self):
        print("Printing vectors...")
        print(self.vecArr)