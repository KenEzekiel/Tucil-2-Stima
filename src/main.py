from Modules.InputHandler import InputHandler
from Modules.Visualizer import visualize3DResult
from Modules.Visualizer import visualize2DResult
from Modules.Visualizer import visualize1DResult
import Modules.DivideAndConquer as Mt
import Modules.Bruteforce as Bf
import time
import numpy as np
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + """
   ________                     __     ____  _      __                      
  / ____/ /___  ________  _____/ /_   / __ \(_)____/ /_____ _____  ________ 
 / /   / / __ \/ ___/ _ \/ ___/ __/  / / / / / ___/ __/ __ `/ __ \/ ___/ _ \\
/ /___/ / /_/ (__  )  __(__  ) /_   / /_/ / (__  ) /_/ /_/ / / / / /__/  __/
\____/_/\____/____/\___/____/\__/  /_____/_/____/\__/\__,_/_/ /_/\___/\___/ 
""" + bcolors.ENDC, end="")

print(bcolors.OKBLUE + """
 __                 ___  ____                     ___             _       __    _          __              
[  |               |_  ||_  _|                  .' _ '.          / \     [  |  (_)        [  |             
 | |.--.   _   __    | |_/ /   .---.  _ .--.    | (_) '___      / _ \     | |  __   .--.   | |--.   ,--.   
 | '/'`\ \[ \ [  ]   |  __'.  / /__\\\[ `.-. |   .`___'/ _/     / ___ \    | | [  | ( (`\]  | .-. | `'_\ :  
 |  \__/ | \ '/ /   _| |  \ \_| \__., | | | |  | (___)  \_   _/ /   \ \_  | |  | |  `'.'.  | | | | // | |, 
[__;.__.'[\_:  /   |____||____|'.__.'[___||__] `._____.\__| |____| |____|[___][___][\__) )[___]|__]\\'-;__/ 
          \__.'                                                                                                                                                                       
""" + bcolors.ENDC)


randomize = input(bcolors.BOLD + bcolors.HEADER +"Randomize vectors? (y/n) : "+bcolors.ENDC)
if (randomize == "y"):
    random = True
    while True:
        n_points = int(input(bcolors.BOLD + bcolors.HEADER +"Enter The Number of Points : "+bcolors.ENDC))
        n_dim = int(input(bcolors.BOLD + bcolors.HEADER +"Enter The Number of Dimensions : "+bcolors.ENDC))
        size = int(input(bcolors.BOLD + bcolors.HEADER +"Enter max threshold size for a point : "+bcolors.ENDC))
        if (n_points > 1 and n_dim > 1 and size >= 1):
            break
        else:
            print(bcolors.BOLD + bcolors.WARNING +"\nPlease enter values correctly!"+bcolors.ENDC)
    useDecimals = input(bcolors.BOLD + bcolors.HEADER +"Use decimals? (y/n) : "+bcolors.ENDC)
    if (useDecimals == "y"):
        decimal = True
    else:
        decimal = False
    Input = InputHandler(n_points, n_dim, size, decimal, random)
else:
    random = False
    filename = input(bcolors.BOLD + bcolors.HEADER +"Enter Filename (no need to use .txt) : "+bcolors.ENDC)
    path = os.path.realpath(__file__)
    direc = os.path.dirname(path)
    direc = direc.replace('src', 'input')
    # print(direc)
    os.chdir(direc)
    vec = []
    with open(f"{direc}/{filename}.txt", 'r') as file:
        for line in file.read().split('\n'):
            # print(line.split(' '))
            vec.append(line.split(' '))        

    vec = np.array(vec).astype(float)
    # print(vec)

    n_points = len(vec)
    # print(n_points)
    n_dim = len(vec[0])
    # print(n_dim)
    size = np.max(vec)
    decimal = True

    Input = InputHandler(n_points, n_dim, size, decimalOn=decimal, randomize=random, inputVector=vec)

showProgress = input(bcolors.BOLD + bcolors.HEADER + "Show progress? [Useful in tracking HUGE vectors which needs > 1000 ops] (y/n) " + bcolors.ENDC)
if (showProgress == "y"):
    Mt.showProgress = True
    Bf.showProgress = True
# Divide and Conquer
print(bcolors.BOLD + bcolors.WARNING + "START CONQUERING!" + bcolors.ENDC)
if Mt.showProgress:
    print("Operations completed: ")
timestart = time.perf_counter()
pair, dist = Mt.getClosestPair(Input.vecArr, Input.num)
timefinish = time.perf_counter()
timeduration = np.round(timefinish - timestart, 5)
print(bcolors.BOLD + bcolors.OKCYAN + "\nclosest distance:" ,dist, bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + "pair of points index:", pair, bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + f"{pair[0]}: {Input.vecArr[pair[0]]}" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + f"{pair[1]}: {Input.vecArr[pair[1]]}" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + "number of operations:", Mt.n, bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + f"time duration: {timeduration} seconds" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + "NOW THE PROBLEM HAS BEEN CONQUERED! DEVIDE ET IMPERA!" + bcolors.ENDC)


# Brute Force
print(bcolors.BOLD + bcolors.WARNING + "\nNow Bruteforcing your way through...." + bcolors.ENDC)
if Bf.showProgress:
    print("Operations completed: ")
timestart = time.perf_counter()
pairBF, distBF = Bf.bruteforce(Input.vecArr)
timefinish = time.perf_counter()
timedurationBF = np.round(timefinish - timestart, 5)
print(bcolors.BOLD + bcolors.OKCYAN + "\nclosest distance:" ,distBF, bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + "pair of points index:", pairBF, bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + f"{pair[0]}: {Input.vecArr[pair[0]]}" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + f"{pair[1]}: {Input.vecArr[pair[1]]}" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + "number of operations:", Bf.n, bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + f"time duration: {timedurationBF} seconds" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + "Oof! That took a lot longer" + bcolors.ENDC)



visualize = input(bcolors.BOLD + bcolors.HEADER + "Visualize points? (y/n) " + bcolors.ENDC)
if (visualize == "y" and Input.dimension == 1):
    visualize1DResult(Input.vecArr, pair)
elif (visualize == "y" and Input.dimension == 2):
    visualize2DResult(Input.vecArr, pair)
elif (visualize == "y" and Input.dimension == 3):
    visualize3DResult(Input.vecArr, pair)
else:
    print(bcolors.BOLD + bcolors.WARNING + "Can't visualize vector!" + bcolors.ENDC)    

fileSave = input(bcolors.BOLD + bcolors.HEADER + "Save results? (y/n) " + bcolors.ENDC)
if (fileSave == "y"):
    filename = input(bcolors.BOLD + bcolors.HEADER +"Enter Filename (no need to use .txt) : "+bcolors.ENDC)
    path = os.path.realpath(__file__)
    direc = os.path.dirname(path)
    direc = direc.replace('src', 'test')
    f = open(f"{direc}/{filename}.txt", 'w')

    f.write(f"Calculated {n_points} points.\n")
    f.write(f"Dimension: {n_dim}\n")
    f.write(f"Threshold: 0-{size} units.\n")
    if decimal:
        f.write(f"Included decimal numbers.\n\n")
    if(dist == distBF):
        f.write("Both methods returns the same results!\n")
    f.write(f"Closest Distance: {dist}\n")
    f.write(f"Pair of points index: {pair}\n")
    f.write(f"{pair[0]}: {Input.vecArr[pair[0]]}\n")
    f.write(f"{pair[1]}: {Input.vecArr[pair[1]]}\n")
    f.write(f"DNC Statistics: {Mt.n} operations at {timeduration} seconds\n")
    f.write(f"BF Statistics: {Bf.n} operations at {timedurationBF} seconds\n")
    print("Saved to files!")
else:
    print(bcolors.BOLD + bcolors.WARNING + "Exiting program..." + bcolors.ENDC)  

Mt.n = 0 # reset the operation counter
Bf.n = 0 # reset the operation counter