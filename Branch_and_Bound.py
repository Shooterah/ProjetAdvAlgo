# Made by : Jeoffrey Pereira
# This function is used to resolve the Knapsack problem with the branch and bound method.
# This method is based on a tree searching algorithm which one is used to check all the possible way to fill the Knapsack.
# Contrary to BrutForce methode this algorithm able to skip some possibility to improve the efficiency.

# Node of the tree and then the subtree of items could be ignored with 2 conditions:
    # I] The left node include an item that overload the sack then the node his ignored
    # II] The max value of the right node subtree is under the best solution already found so all the subtree his ignored

#---------------------------------------------------START OF THE PROGRAM--------------------------------------------------------------#

#---------------------------------------------------------IMPORT----------------------------------------------------------------------#

from traceback import print_tb
import ressources
import random

#---------------------------------------------------------VARIABLE--------------------------------------------------------------------#

# This variable is used to know the Value of all items.
maxValue = 0
# The initalisation of the tree use to found the best items set.
Tree = ressources.Node(None)
# The Combination list with the best Value
Best_Combination = []

#----------------------------------------------------USEFULL-FUNCTION-----------------------------------------------------------------#

# This fonction take the first series of item in the items list to generate a fake best solution with a fake best value (maybe not fake if we are really lucky)
# Then we can use this best combination list and best value to compare it in our main algorithm for the first loop

def tempo_Best_Combination (items):
    current_w = 0
    current_best_value=0
    i = 0
    while (current_w + getattr(items[i],'weight')) < capacity:
        Best_Combination.append(items[i])
        current_w += getattr(items[i],'weight')
        current_best_value += getattr(items[i],'value')
        i = i+1

    return Best_Combination,current_best_value

#-----------------------------------------------------------MAIN----------------------------------------------------------------------#

# Here we get the number of items the knapsack capacity and a list of items composed of positioning in the texte,value and weight. 
nbrItems, capacity, items = ressources.readFileCreateList("Data/low-dimensional/f2_l-d_kp_20_878.txt")

# There we add each item of the list inside the tree and compute the value of all items.
for data in items:
    ressources.Node.addNode(Tree,data)
    maxValue += getattr(data,"value")