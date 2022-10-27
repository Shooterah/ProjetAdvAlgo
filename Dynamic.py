from turtle import clear
import ressources


#Function Dynamic for the initialisation of the table
def DynamicInitTable(items, capacity,nbrItems,Table):
  for i in items:
    #declaration of ind for the indice beetwen 1 and nbrItems
    ind = items.index(i)
    #loop start from 0 to capacity
    for j in range(0,capacity):
      if(j<i.weight):
        Table[ind,j] = Table[ind-1,j]
      else:
        Table[ind,j] = max(Table[ind-1,j],Table[ind-1,int(j-i.weight)]+i.value)

  return Table

#Function to search the best solution in the table
def DynamicSearchSolution(Table,restWeight,nPos,knapsack,items):
  if (Table[nPos,restWeight] == 0):
    return knapsack
  else:
    if(Table[nPos,restWeight] == Table[nPos-1,restWeight]):
      return DynamicSearchSolution(Table,restWeight,nPos-1,knapsack,items)
    else:
      knapsack.append(items[nPos])
      return DynamicSearchSolution(Table,int(restWeight-items[nPos].weight),nPos-1,knapsack,items)



#----#
#Main#
#----#

# Here we create the items that we will use in the knapsack problem and we add them to a list of items
nbrItems, capacity, items = ressources.readFileCreateList("Data/low-dimensional/f4_l-d_kp_4_11.txt")

#add condition if capacity is 0

#some print
print("\n Nbr of items : ",nbrItems)
print("\n Capacity : ",capacity)

#list of items
print("\n List of items : ")
for i in items:
  print(i.printItem())


#create the table of results and initialize it with 0
resTable = np.zeros((nbrItems,capacity))

#afficher la matrice resTable
a = DynamicInitTable(items,capacity,nbrItems,resTable)
print (a)

#green in terminal
print ('\033[92m') 

#Last Value of the table , this is the best Value we have in this configuration
print ("\n BIGGER VALUE : ",a[nbrItems-1,capacity-1])

#standar color in terminal
print ('\033[0m')

knapsack = [] 

finalKnapsack = DynamicSearchSolution(a,int(capacity-1),nbrItems-1,knapsack,items)

print("\n Final knapsack : ")
for i in finalKnapsack:
  print(i.printItem())