from Handler.InputHandler import InputHandler
import MathService as Mt

print("File : \t Input Handler tester")

I1 = InputHandler(3, 4, 100, decimalOn=False)
I2 = InputHandler(5, 3, 10)

I1.printVectors()
I2.printVectors()
# I2.visualizeVectors()

pair, dist = Mt.getClosestPair(I2.vecArr, I2.num)
print(pair, dist)