#!/usr/bin/env python

#
#  +---------------------------------------+
#  |Generator of Data for Knapsack problem |
#  +---------------------------------------+
#
# Variable :
# ----------
#
#   n    = Number of data
#   wmax = Weight max of the data
#   vi   = Value of an item
#   wi   = Weight on an item
#
# Data structure :
# ----------------
#
#   n    wMax
#   vi   wi
#   .    .
#   .    .
#   .    .
#   vn    wn
#
#


#
#  +---------+
#  | Imports |
#  +---------+
#

import sys
import random

#
#  +-----------+
#  | Constants |
#  +-----------+
#

MULTV = 10

MINV = 1
MINW = 1


#
#  +-------------+
#  | Definitions |
#  +-------------+
#

# Manual
def manual() :
    print("> 2 int arguments expected")
    print("> DataGenerator.py n wMax")
    print("> Options :")
    print("     -f : to put filename for the file")

# Define random number
def rand(min,max):
    return random.randint(min,max)

# Create value in string
def createStringValues(wMax, vMax):
    # get the integer value
    w = rand(MINW,wMax)
    v = rand(MINV,vMax)
    # set to a string value
    w = str(w)
    v = str(v)
    return(v + " " + w + "")

# Create a file 
def createFile(wMax, vMax, n, filename) :
    filename = "Data/personal/" + filename
    file = open(filename, "w")
    # First line of the file
    file.write(str(n) + " " + str(wMax))
    for i in range(n) :
        file.write("\n")
        line = createStringValues(wMax, vMax)
        file.write(line)
    file.close()
    return

    

    


#
#  +------+
#  | Main |
#  +------+
#



#print("Begin")


# Verify if the nb of arguments is correct
if len(sys.argv)-1 < 2 :
    print("Not enough arguments (" + str(len(sys.argv)) + "): ")
    manual()
    print("Program failed")
    print("Exit")
    exit()
   
# Define classic filename 
filename = "data.txt"


# Take the values from the command line
n = sys.argv[1]
wMax = sys.argv[2]

# Verify option to able filename
if ((len(sys.argv)-1 > 3) and (sys.argv[3] == "-f")) :
    filename = sys.argv[4]

# Set the (String) values to integers
n = int(n)
wMax = int(wMax)

# vMax value (not to much)
vMax = n * MULTV

# File creation
file = createFile(wMax, vMax, n, str(filename))


## Print the arguments (Not necessary)
#print("Values :")
#print("n =" + str(n))
#print("wMax = " + str(wMax))
#print("vMax = " + str(vMax))


#print("End")


exit()
