import numpy

class InputHandler():
    def __init__(self, num, dimension, size):
        self.num = num
        self.dimension = dimension
        self.size = size
        self.vecArr = []
        self.randomizeVector()
    
    def randomizeVector(self):
        print("Randomizing vectors...")
        self.vecArr = numpy.random.randint(self.size, size=(self.num, self.dimension))

    def printVectors(self):
        print("Printing vectors...")
        print(self.vecArr)