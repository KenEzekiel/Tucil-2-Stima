import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy

def visualize2DResult(vectors: numpy.array, idxpair):
    print("Visualizing Vectors...")
    # Configure Plot
    xres = []
    yres = []
    xdata = []
    ydata = []

    # Set labels
    # plt.set_xlabel('X Label')
    # plt.set_ylabel('Y Label')

    # Data for three-dimensional scattered points
    for i in range(vectors.shape[0]):
        if i in idxpair:
            # data for results
            xres = numpy.append(xres, vectors[i,0])    
            yres = numpy.append(yres, vectors[i,1]) 
        else:
            # data
            xdata = numpy.append(xdata, vectors[i,0])   
            ydata = numpy.append(ydata, vectors[i,1])       

    plt.scatter(xdata, ydata, color= "black", linewidth=0.5)
    plt.scatter(xres, yres, color="green", linewidth=0.5)
    plt.savefig('Visualizer.png', dpi=300) 

    plt.show()

def visualize3DResult(vectors: numpy.array, idxpair):
    print("Visualizing Vectors...")
    # Configure Plot
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    xres = []
    yres = []
    zres = []
    xdata = []
    ydata = []
    zdata = []

    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Data for three-dimensional scattered points
    for i in range(vectors.shape[0]):
        if i in idxpair:
            # data for results
            xres = numpy.append(xres, vectors[i,0])    
            yres = numpy.append(yres, vectors[i,1])
            zres = numpy.append(zres, vectors[i,2])  
        else:
            # data
            xdata = numpy.append(xdata, vectors[i,0])   
            ydata = numpy.append(ydata, vectors[i,1])  
            zdata = numpy.append(zdata, vectors[i,2])        

    ax.scatter(xdata, ydata, zdata, color= "black", linewidth=0.5)
    ax.scatter(xres, yres, zres, color="green", linewidth=0.5)
    plt.savefig('../test/Visualizer.png', dpi=300) 

    plt.show()
    