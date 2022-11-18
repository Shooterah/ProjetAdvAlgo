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

# Evaporation of pheromones
EVAP = 0.2


#
#  +-------------+
#  | Definitions |
#  +-------------+
#

def antColonyWithCycle(liItem, n, wMax, nbAnt, nbCycle):

    # Definitions

    # Max capacity of the bag    
    C = wMax
    # List of objects can be into the knapsack
    N = liItem
    # Current capacity of the bag
    V = C
    # List of object in the knnapsack (partial solution)
    Sp = []
    # List of the best Solution
    Sb = []
    # List of pheromons
    T = []
    # List of probability to go
    P = []







    # For each cycle ( it's a new day for ants in the anthill)
    while(nbCycle > 0):
        # Ants leave the anthill one by one to works ( with a knapsack)
        for i in range(nbAnt):
            # Ant take an empty knapsack
            Sp = []
            # While the knapsack of the ant is not full
            while(V >= 0):








#
#  +------+
#  | Main |
#  +------+
#