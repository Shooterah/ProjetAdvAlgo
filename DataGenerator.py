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

MUTLV = 10

MINV = 1
MINW = 1

#
#  +-------------+
#  | Definitions |
#  +-------------+
#

# Count all the arguments
def nb_args(*args):
    return(len(args))

# Define random number
def random(min,max):
    return random.randint(min,max)

# Create value in string
def createStringValues(wMax, vMax):
    w = random(MINW,wMax)
    v = random(MINV,vMax)
    return(w + " " + v + "")

# Create a file ( a modifier)

fichier = open("data.txt", "r")
    


#
#  +------+
#  | Main |
#  +------+
#

print("Begin")

# Verify if the nb of arguments are correct
if nb_args(sys.argv)+1 < 2 :
    print("Not enough arguments")
    print nb_args(sys.argv)
    exit()

# Take the values from the command line
n = sys.argv[1]
wMax = sys.argv[2]

# vMax value
# Not to much
vMax = n * MultV

# Creation du fichier ( a modifier)
createStringValues(wMax, vMax)

# Print the arguments (Not necessary)
print("Values :")
print("n =" + n)
print("wMax = " + wMax)
print("vMax = " + vMax)

print("End")


exit()
