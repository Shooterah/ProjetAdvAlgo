# Made by : Jeoffrey Pereira
# This function is used to resolve the Knapsack problem with the branch and bound method.
# This method is based on a tree searching algorithm which one is used to check all the possible way to fill the Knapsack.
# Contrary to BrutForce methode this algorithm able to skip some possibility to improve the efficiency.

# Node of the tree and then the subtree of items could be ignored with 2 conditions:
# I] The left node include an item that overload the sack then the node his ignored
# II] The max value of the right node subtree is under the best solution already found so all the subtree his ignored

#---------------------------------------------------START OF THE PROGRAM--------------------------------------------------------------#

#---------------------------------------------------------IMPORT----------------------------------------------------------------------#

from sys import argv
from traceback import print_tb
import ressources
import time


#---------------------------------------------------------VARIABLE--------------------------------------------------------------------#

# This variable is used to know the Value of all items the capacity of the bag and the number of items.
capacity = 0
maxValue = 0
nbrItems = 0
# The initalisation of the tree use to found the best items set.
Tree = ressources.Node(None, None, None, None, None, None)
# The Combination list with the best Value
best_Combination = []
partial_Combination = []
partial_Weight = 0
partial_Value = 0


#----------------------------------------------------USEFULL-FUNCTION-----------------------------------------------------------------#

# This fonction take the first series of item in the items list to generate a fake best solution with a fake best value (maybe not fake if we are really lucky)
# Then we can use this best combination list and best value to compare it in our main algorithm for the first loop

def create_Best_Combination(items):
    best_Weight = 0
    best_Value = 0
    i = 0
    while (best_Weight + getattr(items[i], 'weight')) < capacity:
        best_Combination.append(items[i])
        best_Weight += getattr(items[i], 'weight')
        best_Value += getattr(items[i], 'value')
        i = i+1

    return best_Combination, best_Value, best_Weight


def knapsack(tree, capacity, best_Value, best_Weight, best_Combination, partial_Combination, partial_Weight, partial_Value):

    if tree.CumValue > best_Value and tree.CumWeight <= capacity:
        best_Value = tree.CumValue
        best_Weight = tree.CumWeight
        best_Combination = partial_Combination.copy()
    # Parcourir l'arbre
    if tree.Left_children != None:
        if tree.data != None:
            partial_Combination.append(tree.data)
            partial_Weight += tree.data.weight
            partial_Value += tree.data.value
            best_Combination, best_Value, best_Weight = knapsack(
                tree.Left_children, capacity, best_Value, best_Weight, best_Combination, partial_Combination, partial_Weight, partial_Value)
            partial_Combination.pop()
    if tree.Right_children != None and tree.Right_children.MaxValue > best_Value:
        if tree.data != None:
            best_Combination, best_Value, best_Weight = knapsack(
                tree.Right_children, capacity, best_Value, best_Weight, best_Combination, partial_Combination, partial_Weight, partial_Value)

    return best_Combination, best_Value, best_Weight

#-----------------------------------------------------------MAIN----------------------------------------------------------------------#


def main(type, path):
    global maxValue
    if type == "simple":
        # Here we get the number of items the knapsack capacity and a list of items composed of positioning in the texte,value and weight.
        start = time.time()
        nbrItems, capacity, items = ressources.readFileCreateList(path)
        items.sort(key=lambda x: x.ratio, reverse=True)
        # There we add each item of the list inside the tree and compute the value of all items.
        for i in items:
            maxValue += i.value
        for data in items:
            ressources.Node.addNode(Tree, data, 0, maxValue, 0, None, None)

        best_Combination, best_Value, best_Weight = create_Best_Combination(
            items)
        best_Combination, best_Value, best_Weight = knapsack(
            Tree, capacity, best_Value, best_Weight, best_Combination, partial_Combination, partial_Weight, partial_Value)
        start = time.time() - start
    if type == "multi":
        best_Value = 0
        start = 0
    return start, best_Value
