# Made by : Jeoffrey Pereira
# This function is used to resolve the Knapsack problem with the branch and bound method.
# This method is based on a tree searching algorithm which one is used to check all the possible way to fill the Knapsack.
# Contrary to BrutForce methode this algorithm able to skip some possibility to improve the efficiency.

# Node of the tree and then the subtree of items could be ignored with 2 conditions:
# I] The left node include an item that overload the sack then the node his ignored
# II] The max value of the right node subtree is under the best solution already found so all the subtree are ignored

#---------------------------------------------------START OF THE PROGRAM--------------------------------------------------------------#

#---------------------------------------------------------IMPORT----------------------------------------------------------------------#

from traceback import print_tb
import ressources
import time

#----------------------------------------------------USEFULL-FUNCTION-----------------------------------------------------------------#

# This fonction take the first series of item in the items list to generate a fake best solution with a fake best value (maybe not fake if we are really lucky)
# Then we can use this best combination list and best value to compare it in our main algorithm

def create_Best_Combination(best_Combination,capacity,items):
    best_Weight = 0
    best_Value = 0
    i = 0
    # We create a fake best combination with the first items of the list
    while (best_Weight + getattr(items[i], 'weight')) < capacity:
        best_Combination.append(items[i])
        best_Weight += getattr(items[i], 'weight')
        best_Value += getattr(items[i], 'value')
        # cancel exeption when there is only one item in the list
        if i < len(items) - 1:
            i += 1

    return best_Combination, best_Value, best_Weight

# this function is used to find the best combination of items
# it compose of a tree and a recursive function
# the tree is used to stock all the possible combination of items

def knapsack(tree, capacity, best_Value, best_Weight, best_Combination, partial_Combination, partial_Weight, partial_Value):
    # this is whene we find a better solution
    # we update the best combination,the best value and the best weight
    if tree.CumValue > best_Value and tree.CumWeight <= capacity:
        best_Value = tree.CumValue
        best_Weight = tree.CumWeight
        best_Combination = partial_Combination.copy()
    # we check if the left node is not empty and if the left node is not overloading the sack
    # then we try to add the item of the left node to the partial combination
    if tree.Left_children != None and tree.data != None and tree.Left_children.CumWeight <= capacity:
            partial_Combination.append(tree.data)
            partial_Weight += tree.data.weight
            partial_Value += tree.data.value
            #recursive call
            best_Combination, best_Value, best_Weight = knapsack(
                tree.Left_children, capacity, best_Value, best_Weight, best_Combination, partial_Combination, partial_Weight, partial_Value)
            partial_Combination.pop()
    # we check if the right node is not empty and if the right node is not under the best value already found
    if tree.Right_children != None and tree.Right_children.MaxValue > best_Value and tree.data != None:
            #recursive call
            best_Combination, best_Value, best_Weight = knapsack(
                tree.Right_children, capacity, best_Value, best_Weight, best_Combination, partial_Combination, partial_Weight, partial_Value)

    return best_Combination, best_Value, best_Weight

#-----------------------------------------------------------MAIN----------------------------------------------------------------------#

# Main function of the program which is used to call the other function and to display the result of the program on the graphic interface
def main(type, path):
    # This variable is used to know the Value of all items the capacity of the bag and the number of items.
    capacity = 0
    maxValue = 0
    nbrItems = 0
    # The initalisation of the tree use to found the best items set.
    Tree = ressources.Node(None,None,None, None, None, None, None)
    # The Combination list with the best Value
    best_Combination = []
    # The partial Combination list
    partial_Combination = []
    # the partial weight and value
    partial_Weight = 0
    partial_Value = 0

    # Main for the simple knapsack problem
    if type == "simple":
        # start the timer
        # Here we get the number of items the knapsack capacity and a list of items composed of positioning in the texte,value and weight.
        nbrItems, capacity, items = ressources.readFileCreateList(path)
        # We sort the list of items by value/weight ratio
        items.sort(key=lambda x: x.ratio, reverse=True)
        # We stock the max value of all items
        for i in items:
            maxValue += i.value
        # start the timer
        start = time.time()
        # There we add each item of the list inside the tree and compute the value of all items.
        for data in items:
            ressources.Node.addNode(Tree, data, 0, maxValue, 0, None, None,nbrItems)
        # We create a fake best combination with the first items of the list
        best_Combination, best_Value, best_Weight = create_Best_Combination(best_Combination,capacity,items)
        # We start the recursive function to find the best combination
        best_Combination, best_Value, best_Weight = knapsack(
            Tree, capacity, best_Value, best_Weight, best_Combination, partial_Combination, partial_Weight, partial_Value)
        # stop the timer
        start = time.time() - start

        for i in best_Combination:
            i.printItem()

    # Main for the multiple knapsack problem
    if type == "multi":
        best_Value = 0
        start = 0
    return start, best_Value, nbrItems
