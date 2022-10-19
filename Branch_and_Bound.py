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

#---------------------------------------------------------VARIABLE--------------------------------------------------------------------#

# This variable is used to know the Value of all items the capacity of the bag and the number of items.
maxValue = 0
capacity = 0
nbrItems = 0
# The initalisation of the tree use to found the best items set.
Tree = ressources.Node(None)
# The Combination list with the best Value
best_Combination = []

#----------------------------------------------------USEFULL-FUNCTION-----------------------------------------------------------------#

# This fonction take the first series of item in the items list to generate a fake best solution with a fake best value (maybe not fake if we are really lucky)
# Then we can use this best combination list and best value to compare it in our main algorithm for the first loop

def create_Best_Combination (items):
    current_Weight = 0
    best_Value=0
    i = 0
    while (current_Weight + getattr(items[i],'weight')) < capacity:
        best_Combination.append(items[i])
        current_Weight += getattr(items[i],'weight')
        best_Value += getattr(items[i],'value')
        i = i+1

    return best_Combination,best_Value,current_Weight

# This fonction generate an empty solution

def create_Partial_Combination():
    partial_Weight = 0
    partial_Value=0
    partial_Combination = []

    return partial_Combination,partial_Value,partial_Weight



def KnapSack(best_Combination,best_Value,best_Weight,partial_Combination,partial_Value,partial_Weight,Tree,current_value):

    if partial_Value >= best_Value :
        best_Value = partial_Value
        best_Weight = partial_Weight
        best_Combination = partial_Combination[:]
        print(best_Value)
    else:
        if  getattr(Tree,"Right_children") is not None and getattr(Tree,"Left_children") is not None:
            if partial_Weight + getattr(getattr(Tree,"data"),"weight") <= capacity:
                if current_value - getattr(getattr(Tree,"data"),"value") >= best_Value:
                    partial_Combination,partial_Value,partial_Weight = KnapSack(best_Combination,best_Value,best_Weight,partial_Combination,partial_Value,partial_Weight,getattr(Tree,"Right_children"),current_value-getattr(getattr(Tree,"data"),"value"))
                    item = ressources.item(getattr(getattr(Tree,"data"),"pos"),getattr(getattr(Tree,"data"),"value"),getattr(getattr(Tree,"data"),"weight"))
                    partial_Combination.append(item)
                    partial_Value = partial_Value + getattr(item,"value")
                    partial_Weight = partial_Weight + getattr(item,"weight")
                    partial_Combination,partial_Value,partial_Weight = KnapSack(best_Combination,best_Value,best_Weight,partial_Combination,partial_Value,partial_Weight,getattr(Tree,"Left_children"),current_value)
                else : 
                    item = ressources.item(getattr(getattr(Tree,"data"),"pos"),getattr(getattr(Tree,"data"),"value"),getattr(getattr(Tree,"data"),"weight"))
                    partial_Combination.append(item)
                    partial_Value = partial_Value + getattr(item,"value")
                    partial_Weight = partial_Weight + getattr(item,"weight")
                    partial_Combination,partial_Value,partial_Weight = KnapSack(best_Combination,best_Value,best_Weight,partial_Combination,partial_Value,partial_Weight,getattr(Tree,"Left_children"),current_value)
        return partial_Combination,partial_Value,partial_Weight
    return best_Combination,best_Value,best_Weight
            





#-----------------------------------------------------------MAIN----------------------------------------------------------------------#

# Here we get the number of items the knapsack capacity and a list of items composed of positioning in the texte,value and weight. 
nbrItems, capacity, items = ressources.readFileCreateList("Data/low-dimensional/f2_l-d_kp_20_878.txt")

# There we add each item of the list inside the tree and compute the value of all items.
for data in items:
    ressources.Node.addNode(Tree,data)
    maxValue += getattr(data,"value")



best_Combination,best_Value,best_Weight = create_Best_Combination(items)
partial_Combination,partial_Value,partial_Weight = create_Partial_Combination()


best_Combination,test1,test2 = KnapSack(best_Combination,best_Value,best_Weight,partial_Combination,partial_Value,partial_Weight,Tree,maxValue)


print("value "+str(test1))
print("weight "+str(test2))
print(best_Value)
print(maxValue)