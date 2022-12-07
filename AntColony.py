#!/usr/bin/env python

#
#  +---------------------------------+
#  | Ant Colony for Knapsack problem |
#  +---------------------------------+
#
# Arguments :
# -----------
#
#   path = path of the file
#

#
#  +---------+
#  | Imports |
#  +---------+
#

import sys
import ressources
import time

from random import random



#
#  +-----------+
#  | Constants |
#  +-----------+
#

# Color for terminal
# from : https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
CRED = '\033[91m'
CBLUE = '\033[94m'
CCYAN = '\033[96m'
CGREEN = '\033[92m'
CEND = '\033[0m'
UNDERLINE = '\033[4m'
BOLD = '\033[1m'

# Number of ANTS
ANTS = 20

# Nubmer of cycles
CYCLES = 3

# Choice of the attractive strenght
RATIO = 1
VALUE = 2
WEIGHT = 3

# Evaporation of pheromones [0-1]
EVAP = 0.01

# Initial state of pheromones
PHERO = 1


#
#  +-------------+
#  | Definitions |
#  +-------------+
#

# Dsipaly manual
def manual() :
    print("Manual :")
    #print(" > 1 option (String) of attractive strenght expected")
    print(" > 1 path (String) argument expected")
    print(" > AntColony.py path")

# Display Error message
def error() :
    print(f"{CRED}--------------")
    print("/!\\ Error /!\\")
    print(f"--------------{CEND}")

# Display exiting program message
def exitProg() :
    print(f"{CRED}Program failed")
    print(f"Exit.{CEND}")
    exit()

# Display Item list
def disItLi(itemLi):
    ressources.fullLine(90)
    for item in itemLi :
        item.printItem()
    ressources.fullLine(90)




# # Create the list of probability with attractive ratio
# def makePratio(liItem,n, trail):
#     #P = [PHERO for i in range(n)]
#     P = []
#     tmp = 0
#     # Init the probability value
#     for i in range(n):
#         P.append(trail*liItem[i].ratio)
#         tmp += trail*liItem[i].ratio
#     # Divisions by the total
#     for i in range(n):
#         P[i] /= tmp
#     return P

# # Create the list of probability with attractive value
# def makePvalue(liItem,n, trail):
#     P = []
#     tmp = 0
#     # Init the probability value
#     for i in range(n):
#         P.append(trail*liItem[i].value)
#         tmp += trail*liItem[i].value
#     # Divisions by the total
#     for i in range(n):
#         P[i] /= tmp
#     return P

# # Create the list of probability with attractive weight
# def makePweight(liItem,n,trail):
#     P = []
#     tmp = 0
#     # Init the probability value
#     for i in range(n):
#         P.append(trail*liItem[i].weight)
#         tmp += trail*liItem[i].weight
#     # Divisions by the total
#     for i in range(n):
#         P[i] /= tmp
#     return P

# Create list of pheromones
def initT(phero,n):
    T = []
    for i in range(n):
        T.append(phero)
    return T


# Create the list of strenght attractivity
def initL(liItem, n, type):
    L=[]

    # Case of Ratio
    if(type == RATIO):
        for i in range(n):
            L.append(liItem[i].ratio)
    # Case of Value
    elif(type == VALUE):
        for i in range(n):
            L.append(liItem[i].value)
    # acse of weight
    elif(type == WEIGHT):
        for i in range(n):
            L.append(liItem[i].weight)
    else:
        error()
        print(f"\tThe type: {type} for the function makeP(liItem, n, type) doesn't exist...")
        exitProg()
    return L

# Init Probability list
def initP(L, n):
    P = []
    for i in range(n):
        P.append(L[i])
    return P

# Create the list of probability
def updateP(P, T, L, n):
    # Caclulate inital probability list
    for i in range(n):
        P[i] = (T[i]*L[i])
    # Calculate total
    tmp = sum(P)
    if(tmp != 0):
        # Update the final probability list
        for i in range(n):
            P[i] /= tmp

    return P



# Update the list of trail
# Zgb = Glbobal better solution
# Zb  = Betetr solution
def updateT(T, S, Zgb, Zb):
    # For each element in the solution
    for i in S:
        T[i] += 1/(1+((Zgb-Zb)/Zgb))
    return T


def removeBig(liItem, L, V, n):
    # Analize each element of L if one is too fat
    for i in range(n):
        if(liItem[i].weight > V and L[i] != 0):
            L[i] = 0
    return L


# Evaporation of pheromones
def evapT(T, n, ev):
    for i in range(n):
        T[i] *= ev
    return T

# Update the trail of pheromones
# def updateTrail(P, Zgb, Zb, Sb,T):
#     for i in Sb:
#         T[i] += 1/(1+((Zgb-Zb)/Zgb))
#     return P


# Choose the next element from Pj randomly
def chooseNext(Pj):
    # Take a value (float) between [0.0-1.0]
    rand = random()
    # print("\n \n")
    # print(rand)
    # print(Pj)
    # Iteration to match random number with the list of probability
    tmp = 0
    ind = 0 # stock index
    for i in Pj:
        tmp += i
        # print(tmp)
        if(rand < tmp):
             return ind
        ind += 1
    # If it's the last element
    ind -= 1
    return ind





def antColonyWithCycle(liItem, n, wMax, nbAnt, nbCycle):

    # Stock the time when function start
    start_time = time.time()

    # Definitions

    # List of pheromons
    T = initT(PHERO,n)
    # List of attractivity
    L = initL(liItem, n, RATIO)
    # List of Probability
    P = initP(L, n)



    # Max capacity of the bag
    C = wMax
    # List of objects can be into the knapsack
    N = liItem

    # List of the best Solution
    Sb = []
    # Maximum profit found
    Zb = 0
    # Global (For all cycle) maximum profit
    Zgb = 0
    # Global (For all cycle) better solution
    Sgb = []
    # Current profit of the ant
    Zc = 0
    # Current capacity of the bag
    V = C
    # List of object in the knnapsack (partial solution)
    Sp = []

    trail = PHERO
    evap = EVAP

    # For each cycle ( it's a new day for ants in the anthill)
    while(nbCycle > 0):
        # Ants leave the anthill one by one to works ( with a knapsack)
        for i in range(nbAnt):
            # Ant take an empty knapsack
            Sp = []
            V = C
            Zc = 0
            # List of pheromons
            T = initT(PHERO,n)
            # List of attractivity
            L = initL(liItem, n, RATIO)
            # While the knapsack of the ant is not full

            # print(f"Debut {Zc}")

            while(V > 0):
                # Ant take the list of probability
                P = updateP(P, T, L, n)
                # Ant determine the next element (choose the index of the next element)
                ind = chooseNext(P)
                # Youhou ! Let's go ! The ant took an element
                Sp.append(ind)
                Zc += liItem[ind].value
                # Ant remove the actual element from this "map"
                L[ind] = 0
                # The knapsack capacity is decrease and it become more heavy for the ant
                V -= liItem[ind].weight  
                # The ant erase all the element who cannot be choose
                L = removeBig(liItem, L, V, n)
                # If L is like empty
                if(sum(L) == 0):
                    break
            # Find the best of the day
            if(Zb < Zc):
                # Update the better profit
                Zb = Zc
                # Update the better solution
                Sb = Sp
        # Compare the best of the day with the best of thes cycles
        if(Zgb < Zb):
            Zgb = Zb
            Sgb = Sb
        # Decrease the cycle ( it's de night for the anthill, all the ants go to sleep)
        nbCycle -= 1
        # During the night the pheromones evaporate
        T = evapT(P,n,evap)
        # Also some ants do the 3x8 and update the trail of pheromone for tomorrow
        T = updateT(T, Sgb, Zgb, Zb)
        # print(T)




    vTot = Zgb
    res = Sgb

    # Stock timer now
    end_time = time.time()
    tExec = end_time - start_time

    return vTot, res, tExec





#
#  +------+
#  | Main |
#  +------+
#
# #Verify if the nb of arguments is correct
# if len(sys.argv)-1 < 1 :
#     error()
#     print("Not enough arguments (" + str(len(sys.argv)) + "): ")
#     manual()
#     exitProg()

# # Authorized option
# AuthOpt = ['a','v','w','r']

# # Get the option of AntColony version
# opt = sys.argv[1]

# # Verify if the option is valid
# if ((len(opt)!=2) or (opt[1] not in AuthOpt)):
#     error()
#     print("The option need to be one character :")
#     print("\t -a : all attractive strength available")
#     print("\t -v : only value attractive strenght")
#     print("\t -w : only weights attractive strength")
#     print("\t -r : only ratios attractive strenght\n")
#     manual()
#     exitProg()

# opt = opt[1]

def main(type, path):
    # Get the path of the file
    if type == 'simple':
        # Check if the path is correct
        try :
            # Stock values of the file
            n, wMax, liItem = ressources.readFileCreateList(path)
        except :
            error()
            print("\tThe path doesn't exist")
            exitProg()

        # Result
        # print(f"{UNDERLINE}{BOLD}\nEvaluation with Ant Colony Optimization algorithm using ratios for attractive strenght:\n{CEND}")

        vTot, res, tExec = antColonyWithCycle(liItem, n, wMax, ANTS, CYCLES)

        # print(f"\nMaximum value result : {CBLUE}{BOLD}{vTot}{CEND}")
        # print(f"List of result (From the initial file): {CBLUE}{BOLD}{res}{CEND}")
        # print(f"Time of execution : {CGREEN}{tExec}{CEND} s")
        # print(f"Time of execution : {CGREEN}{tExec*1000}{CEND} ms")


        # print(f"{UNDERLINE}\nInitial parameters :{CEND}")
        # print(f"  n    : {BOLD}{n}{CEND}")
        # print(f"  wMax : {BOLD}{wMax}{CEND}")
    if type == "multi":
        vTot = 0
        tExec = 0

    return tExec, vTot, n



#
#  +------+
#  | Main |
#  +------+
#


# #Verify if the nb of arguments is correct
# if len(sys.argv)-1 < 1 :
#     error()
#     print("Not enough arguments (" + str(len(sys.argv)) + "): ")
#     manual()
#     exitProg()

# # Authorized option
# AuthOpt = ['a','v','w','r']

# # Get the option of AntColony version
# opt = sys.argv[1]

# # Verify if the option is valid
# if ((len(opt)!=2) or (opt[1] not in AuthOpt)):
#     error()
#     print("The option need to be one character :")
#     print("\t -a : all attractive strength available")
#     print("\t -v : only value attractive strenght")
#     print("\t -w : only weights attractive strength")
#     print("\t -r : only ratios attractive strenght\n")
#     manual()
#     exitProg()

# opt = opt[1]

def main2():
    # Verify if the nb of arguments is correct
    if len(sys.argv)-1 < 1 :
        error()
        print("Not enough arguments (" + str(len(sys.argv)) + "): ")
        manual()
        exitProg()


    # Get the path of the file
    path = sys.argv[1]

    # Check if the path is correct
    try :
        # Stock values of the file
        n, wMax, liItem = ressources.readFileCreateList(path)
    except :
        error()
        print("\tThe path doesn't exist")
        exitProg()



    # Result

    print(f"{UNDERLINE}{BOLD}\nEvaluation with Ant Colony Optimization algorithm using ratios for attractive strenght:\n{CEND}")

    vTot, res, tExec = antColonyWithCycle(liItem, n, wMax, ANTS, CYCLES)

    print(f"\nMaximum value result : {CBLUE}{BOLD}{vTot}{CEND}")
    print(f"List of result (From the initial file): {CBLUE}{BOLD}{res}{CEND}")
    print(f"Time of execution : {CGREEN}{tExec}{CEND} s")
    print(f"Time of execution : {CGREEN}{tExec*1000}{CEND} ms")


    print(f"{UNDERLINE}\nInitial parameters :{CEND}")
    print(f"  n    : {BOLD}{n}{CEND}")
    print(f"  wMax : {BOLD}{wMax}{CEND}")