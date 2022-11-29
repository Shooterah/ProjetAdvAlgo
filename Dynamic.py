# Made by Arthur Micol
import ressources
import time

# Function Dynamic (be care u can only use file where the weight isn't a float)
# O(nW)time and O(nW)space

# not really polynomial(runtime grows as inpout size grows, problem of space complexity)
# add dynamic top and down

# Function Dynamic for the initialisation of the table


def DynamicInitTable(items, capacity, nbrItems, Table):
    for i in items:
        # declaration of ind for the indice beetwen 1 and nbrItems
        ind = items.index(i)
        # loop start from 0 to capacity
        for j in range(1, capacity):
            if (j < i.weight):
                Table[ind, j] = Table[ind-1, j]
            else:
                Table[ind, j] = max(
                    Table[ind-1, int(j-i.weight)]+i.value, Table[ind-1, j])

    return Table

# Function to search the best solution in the table


def DynamicSearchSolution(Table, restWeight, nPos, knapsack, items):
    # solution for the moment where we are in the first column and when we can't call npos-1
    if (nPos == 0):
        if (Table[nPos, restWeight] > 0):
            knapsack.append(items[nPos])
        return knapsack

    # for the rest of the table
    if (Table[nPos, restWeight] == 0):
        return knapsack
    else:
        if (Table[nPos, restWeight] == Table[nPos-1, restWeight]):
            return DynamicSearchSolution(Table, restWeight, nPos-1, knapsack, items)
        else:
            knapsack.append(items[nPos])
            return DynamicSearchSolution(Table, int(restWeight-items[nPos].weight), nPos-1, knapsack, items)


#----#
#Main#
#----#
def main(type, path):
    # add condition if capacity is 0
    if type == "simple":
        # Here we get the number of items the knapsack capacity and a list of   items composed of positioning in the texte,value and weight.
        start = time.time()
        nbrItems, capacity, items = ressources.readFileCreateList(path)
        # create the table of results and initialize it with 0 (capcity +1 because we start from 0)
        resTable = np.zeros((nbrItems, capacity+1))
        # fill the table with the dynamic function
        a = DynamicInitTable(items, capacity+1, nbrItems, resTable)

        # avoir le knapsack
        knapsack = []
        finalKnapsack = DynamicSearchSolution(
            a, int(capacity), nbrItems-1, knapsack, items)
        MaxValue = a[nbrItems-1, capacity]
        start = time.time() - start
    if type == "multi":
        best_Value = 0
        start = 0
    return start, MaxValue
