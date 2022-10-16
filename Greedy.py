#!/usr/bin/env python

#
#  +---------------------------------------+
#  | Greedy algorithm for Knapsack problem |
#  +---------------------------------------+
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


#
#  +-------------+
#  | Definitions |
#  +-------------+
#

# Dsipaly manual
def manual() :
    print("Manual :")
    print(" > 1 option (String) of greedy expected")
    print(" > 1 path (String) argument expected")
    print(" > Greedy.py path")
    
# Display Error message
def error() : 
    print(CRED + "--------------" )
    print("/!\\ Error /!\\")
    print("--------------"+CEND)

# Display exiting program message
def exitProg() :
    print(CRED + "Program failed")
    print("Exit." + CEND)
    exit()
    
# Display Item list
def disItLi(itemLi):
    ressources.fullLine(90)
    for item in itemLi :
        item.printItem()
    ressources.fullLine(90)

    
# Greedy 1 :
# Use a dataset with values are sort in decreasing order
# Keep all the first values iteratievly
def greedy1(liItem, n, wMax):
    
    # Init list of resultat
    res = [] 
    # Init total value
    vTot = 0
    # Init iterator
    i = 0
     
    # Copy the initial list 
    sortV = liItem.copy()
    # Sort a list by value in reverse 
    sortV.sort(key=lambda x: x.value, reverse = True)
    
    #Display sort list
    disItLi(sortV)
    
    # Iteration on the list
    while( i < n and wMax > 0):
        # Can we add the element ?
        if ( (wMax-sortV[i].weight) >= 0 ):
            # Add the initial pos to res
            res.append(sortV[i].pos)
            # Decrease the capacity of knapsack
            wMax -= sortV[i].weight
            # Increase the total value
            vTot += sortV[i].value
        # Increase iterator 
        i += 1
    return vTot, res


# Greedy 2 :
# Use a dataset with weights are sort in increasing order
# Keep all the first values iteratievly
def greedy2(liItem, n, wMax):
    
    # Init list of resultat
    res = [] 
    # Init total value
    vTot = 0
    # Init iterator
    i = 0
     
    # Copy the initial list 
    sortW = liItem.copy()
    # Sort a list by weight  
    sortW.sort(key=lambda x: x.weight)
    
    #Display sort list
    disItLi(sortW)
    
    # Iteration on the list
    while( i < n and wMax > 0):
        # Can we add the element ?
        if ( (wMax-sortW[i].weight) >= 0 ):
            # Add the initial pos to res
            res.append(sortW[i].pos)
            # Decrease the capacity of knapsack
            wMax -= sortW[i].weight
            # Increase the total value
            vTot += sortW[i].value
        # Increase iterator 
        i += 1
    return vTot, res



# Greedy 3 :
# Use a dataset with ratio are sort in decreasing order
# Keep all the first values iteratievly
def greedy3(liItem, n, wMax):
    
    # Init list of resultat
    res = [] 
    # Init total value
    vTot = 0
    # Init iterator
    i = 0
    
    # Copy the initial list 
    sortR = liItem.copy()
    # Sort a list by weight  
    sortR.sort(key=lambda x: x.ratio, reverse = True)
    
    #Display sort list
    disItLi(sortR)
    
    # Iteration on the list
    while( i < n and wMax > 0):
        # Can we add the element ?
        if ( (wMax-sortR[i].weight) >= 0 ):
            # Add the initial pos to res
            res.append(sortR[i].pos)
            # Decrease the capacity of knapsack
            wMax -= sortR[i].weight
            # Increase the total value
            vTot += sortR[i].value
        # Increase iterator 
        i += 1
    return vTot, res




#
#  +------+
#  | Main |
#  +------+
#


# Verify if the nb of arguments is correct
if len(sys.argv)-1 < 1 :
    error()
    print("Not enough arguments (" + str(len(sys.argv)) + "): ")
    manual()
    exitProg()
    
# Authorized option
AuthOpt = ['a','v','w','r']
   
# Get the option of greedy version
opt = sys.argv[1]

# Verify if the option is valid
if ((len(opt)!=2) or (opt[1] not in AuthOpt)):
    error()
    print("The option need to be one character :")
    print("\t -a : all greedys resolution")
    print("\t -v : only values greedy resolution")
    print("\t -w : only weights greedy resolution")
    print("\t -r : only ratios greedy resolution\n")
    manual()
    exitProg()
    
opt = opt[1]
    
# Get the path of the file
path = sys.argv[2]

# Check if the path is correct
try :
    # Stock values of the file
    n, wMax, liItem = ressources.readFileCreateList(path)
except :
    error()
    print("\tThe path doesn't exist")
    exitProg()


#
#   Knapsack problem resolution with greedy 
#   ---------------------------------------

# Result with Greedy 1 ( option : 'a' or 'v') :
if (opt == 'a' or opt == 'v'):
    print(UNDERLINE + BOLD + "\nEvaluation with greedy algorithm using values :\n" + CEND)
    vTot, res = greedy1(liItem, n ,wMax)
    print("\nMaximum result : " + CBLUE + BOLD + str(vTot) + CEND)
    print("List of result (From the initial file): " + CBLUE + BOLD + str(res) + CEND)
    
# Result with Greedy 2 ( option : 'a' or 'w') : 
if (opt == 'a' or opt == 'w'):
    print(UNDERLINE + BOLD + "\nEvaluation with greedy algorithm using weights :\n" + CEND)
    vTot, res = greedy2(liItem, n ,wMax)
    print("\nMaximum result : " + CBLUE + BOLD + str(vTot) + CEND)
    print("List of result (From the initial file): " + CBLUE + BOLD + str(res) + CEND)

# Result with Greedy 3 ( option : 'a' or 'r') :
if (opt == 'a' or opt == 'r'):
    print(UNDERLINE + BOLD + "\nEvaluation with greedy algorithm using ratios :\n" + CEND)
    vTot, res = greedy3(liItem, n ,wMax)
    print("\nMaximum result : " + CBLUE + BOLD + str(vTot) + CEND)
    print("List of result (From the initial file): " + CBLUE + BOLD + str(res) + CEND)
  
print(UNDERLINE + "\nInitial parameters :" + CEND)  
print("  n    : " + BOLD + str(n) + CEND)
print("  wMax : " + BOLD + str(wMax) + CEND)
    
#print("End")
