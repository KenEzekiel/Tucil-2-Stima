import numpy

class InputHandler():
    def __init__(self, num: int, dimension: int, size: int, decimalOn=True):
        self.num = num
        self.dimension = dimension
        self.size = size
        self.vecArr = []
        self.randomizeVector()
        if not decimalOn:
            self.vecArr = numpy.round(self.vecArr)
        else:
            self.vecArr = numpy.round(self.vecArr, 3)
    
    def randomizeVector(self):
        print("Randomizing vectors...")
        self.vecArr = numpy.random.rand(self.num, self.dimension)
        self.vecArr = self.size * self.vecArr

    def printVectors(self):
        print("Printing vectors...")
        print(self.vecArr)