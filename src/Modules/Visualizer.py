import matplotlib.pyplot as plt
import numpy
from mpl_toolkits import mplot3d

def visualize1DResult(vectors: numpy.array, idxpair):
    print("Visualizing Vectors...")
    val = 0
    xres = []
    xdata = []
    for i in range(vectors.shape[0]):
        if i in idxpair:
            # data for results
            xres = numpy.append(xres, vectors[i,0])    
        else:
            # data
            xdata = numpy.append(xdata, vectors[i,0])   
    plt.scatter(xdata, numpy.zeros_like(xdata) + val, color='black')
    plt.scatter(xres, numpy.zeros_like(xres) + val, color='green')
    plt.show()

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

    # Data for two-dimensional scattered points
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
    count = 0
    RGB = [0,0,0]
    xres = []
    yres = []
    zres = []
    xdata = []
    ydata = []
    zdata = []
    x = []
    y = []
    z = []

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
            count += 1
            if (count % 2 == 1):
                RGB[count % 3] = numpy.random.uniform(0.3, 1.0)
                x = []
                y = []
                z = []
                x = numpy.append(x, vectors[i,0]) 
                y = numpy.append(y, vectors[i,1])
                z = numpy.append(z, vectors[i,2])
            else:
                x = numpy.append(x, vectors[i,0]) 
                y = numpy.append(y, vectors[i,1])
                z = numpy.append(z, vectors[i,2])
                ax.plot(x, y, z, color='green')
        else:
            # data
            xdata = numpy.append(xdata, vectors[i,0])   
            ydata = numpy.append(ydata, vectors[i,1])  
            zdata = numpy.append(zdata, vectors[i,2])        

    ax.scatter(xdata, ydata, zdata, color= "black", linewidth=0.5)
    ax.scatter(xres, yres, zres, color=RGB, linewidth=0.5)
    plt.savefig(f"Visualizer.png", dpi=300) 

    plt.show()
    