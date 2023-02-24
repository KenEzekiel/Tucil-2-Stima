# Importing Libraries
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

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
        self.vecArr = numpy.sort(self.vecArr, axis=0)
    
    def randomizeVector(self):
        print("Randomizing vectors...")
        self.vecArr = numpy.random.rand(self.num, self.dimension)
        self.vecArr = self.size * self.vecArr

    def printVectors(self):
        print("Printing vectors...")
        print(self.vecArr)

    def visualizeVectors(self):
        print("Visualizing Vectors...")
        # Configure Plot
        fig = plt.figure()
        ax = plt.axes(projection='3d')

        # Set labels
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        # Data for three-dimensional scattered points
        xdata = self.vecArr[:,0]
        ydata = self.vecArr[:,1]
        zdata = self.vecArr[:,2]

        ax.scatter(xdata, ydata, zdata, c=zdata, cmap='viridis', linewidth=0.5)


        plt.show()

    

    