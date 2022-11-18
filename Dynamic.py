import numpy as np
import ressources
# Function Dynamic (be care u can only use file where the weight isn't a float)
# O(nW)time and O(nW)space

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
# Here we create the items that we will use in the knapsack problem and we add them to a list of items
nbrItems, capacity, items = ressources.readFileCreateList(
    #    "Data/low-dimensional/f8_l-d_kp_23_10000.txt")
    "Data/low-dimensional/test_arthur.txt")

# add condition if capacity is 0

# some print
print("\n Nbr of items : ", nbrItems)
print("\n Capacity : ", capacity)

# list of items
print("\n List of items : ")
for i in items:
    print(i.printItem())


# create the table of results and initialize it with 0 (capcity +1 because we start from 0)
resTable = np.zeros((nbrItems, capacity+1))

# print the matrice resTable
print("\n Matrice : ")
a = DynamicInitTable(items, capacity+1, nbrItems, resTable)
print(a)

#green in terminal
print('\033[92m')

# Last Value of the table , this is the best Value we have in this configuration
print("\n BIGGER VALUE : ", a[nbrItems-1, capacity])

# standar color in terminal
print('\033[0m')

knapsack = []

finalKnapsack = DynamicSearchSolution(
    a, int(capacity), nbrItems-1, knapsack, items)

print("\n Final knapsack : ")
for i in finalKnapsack:
    print(i.printItem())
