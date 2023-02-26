from Handler.InputHandler import InputHandler
import numpy
import MathService as Mt
import time

print("File : \t Input Handler tester")

I1 = InputHandler(6, 4, 100)
I2 = InputHandler(5, 3, 10)

I1.printVectors()
I2.printVectors()
I2.visualizeVectors()

timestart = time.perf_counter()
pair, dist = Mt.getClosestPair(I1.vecArr, I1.num)
timefinish = time.perf_counter()
timeduration = numpy.round(timefinish - timestart, 5)
print(pair, dist, Mt.n, timeduration, "s")
Mt.n = 0
print("reset n", Mt.n)

timestart = time.perf_counter()
pair, dist = Mt.getClosestPairParent(I1.vecArr, I1.num)
timefinish = time.perf_counter()
timeduration = numpy.round(timefinish - timestart, 5)
print(pair, dist, Mt.n, timeduration, "s")