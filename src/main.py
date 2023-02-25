from Handler.InputHandler import InputHandler
import MathService as Mt
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
    n_points = int(input(bcolors.BOLD + bcolors.HEADER +"Enter The Number of Points : "+bcolors.ENDC))
    n_dim = int(input(bcolors.BOLD + bcolors.HEADER +"Enter The Number of Dimensions : "+bcolors.ENDC))
    size = int(input(bcolors.BOLD + bcolors.HEADER +"Enter max threshold size for a point : "+bcolors.ENDC))
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
    with open(f"{direc}\\{filename}.txt", 'r') as file:
        for line in file.read().split('\n'):
            print(line.split(' '))
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

# Divide and Conquer
print(bcolors.BOLD + bcolors.WARNING + "START CONQUERING!" + bcolors.ENDC)
timestart = time.perf_counter()
pair, dist = Mt.getClosestPair(Input.vecArr, Input.num)
timefinish = time.perf_counter()
timeduration = np.round(timefinish - timestart, 5)
print(bcolors.BOLD + bcolors.OKCYAN + "closest distance:" ,dist, bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + "pair of points index:", pair, bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + f"{pair[0]}: {Input.vecArr[pair[0]]}" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + f"{pair[1]}: {Input.vecArr[pair[1]]}" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + "number of operations:", Mt.n, bcolors.ENDC)
print(bcolors.BOLD + bcolors.OKCYAN + f"time duration: {timeduration} seconds" + bcolors.ENDC)
print(bcolors.BOLD + bcolors.WARNING + "NOW THE PROBLEM HAS BEEN CONQUERED! DEVIDE ET IMPERA!" + bcolors.ENDC)

# Brute Force
Mt.n = 0 # reset the operation counter


visualize = input(bcolors.BOLD + bcolors.HEADER + "Visualize points? (y/n) " + bcolors.ENDC)
if (visualize == "y" and Input.dimension <= 3):
    Input.visualizeVectors()
else:
    print(bcolors.BOLD + bcolors.WARNING + "Can't visualize vector!" + bcolors.ENDC)    

