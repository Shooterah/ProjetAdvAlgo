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

# Color for terminal (for error)
CRED = '\033[91m'
CEND = '\033[0m'

#
#  +-------------+
#  | Definitions |
#  +-------------+
#

# Dsipaly manual
def manual() :
    print(" > 2 path argument expected")
    print(" > Greedy.py path")
    #print("> Options :")
    
# Display Error message
def error() : 
    print(CRED + "--------------" + CEND)
    print(CRED + "/!\\ Error /!\\" + CEND)
    print(CRED + "--------------" + CEND)

# Display exiting program message
def exitProg() :
    print(CRED + "Program failed" + CEND)
    print(CRED + "Exit." + CEND)
    exit()
    
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

print("n : " + str(n))
print("wMax : " + str(wMax))


#
#   Sort of list
#   ------------
 
 # Sort a list by value in reverse (1)   
sortV = liItem.copy()
sortV.sort(key=lambda x: x.value, reverse = True)

# Sort a list by weight (2)
sortW = liItem.copy() 
sortW.sort(key=lambda x: x.weight)

# Sort the list by ratio (3)
sortR = liItem.copy()
sortR.sort(key=lambda x: x.ratio)


for item in sortV :
    item.printItem()
print("------")
for item in sortW :
    item.printItem()
print("------")
for item in sortR :
    item.printItem()
print("------")
    
print("End")
