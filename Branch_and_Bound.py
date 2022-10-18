# Made by : Jeoffrey Pereira
# This function is used to resolve the Knapsack problem with the branch and bound method.
# This method is based on a tree searching algorithm which one is used to check all the possible way to fill the Knapsack.
# Contrary to BrutForce methode this algorithm able to skip some possibility to improve the efficiency.

# Node of the tree and then the subtree of items could be ignored with 2 conditions:
    # I] The left node include an item that overload the sack then the node his ignored
    # II] The max value of the right node subtree is under the best solution already found so all the subtree his ignored

#---------------------------------------------------START OF THE PROGRAM--------------------------------------------------------------#
import ressources

# This variable is used to know the Value of all items.
maxValue = 0

# Here we get the number of items the knapsack capacity and a list of items composed of positioning in the texte,value and weight. 
nbrItems, capacity, items = ressources.readFileCreateList("Data/low-dimensional/f3_l-d_kp_4_20.txt")

# The initalisation of the tree use to found the best items set.
Tree = ressources.Node(None)

# There we add each item of the list inside the tree and compute the value of all items.
for data in items:
    ressources.Node.addNode(Tree,data)
    maxValue += getattr(data,"value")

