import sys
import time
import ressources


#################################################
############### SIMPLE KNAPSACK #################
#################################################

# This function is used to brute force the Knapsack problem
# It takes the list of items and the capacity of the knapsack as parameters
# It returns the list of items that are in the knapsack
# It returns an empty list if no solution is found
# Its complexity is O(2^n)
# So it means that if we have 10 items, it will take 1024 operations to find the solution
# If we have 20 items, it will take 1,048,576 operations to find the solution
# If we have 30 items, it will take 1,073,741,824 operations to find the solution
# So it is very slow
# I think it is not recommended to use it with more than 20 items, but it always gives the optimal solution
def bruteForce(capacity, items):

    # Calculate the time of execution
    start_time = time.time()

    # Create a list of all possible combinations of items
    combinaisons = []

    # Create a list of all possible combinations of items that fit in the knapsack
    combinaisonsPossibles = []

    # Create a list of all possible combinations of items that fit in the knapsack and that have the highest value
    combinaisonsPossiblesMax = []

    # We initialize the highest combination value to 0
    valeurMax = 0

    # We know that all possible combinations of items are 2^n
    # We create a list of all possible combinations of items
    # We use the binary system to create all possible combinations of items
    # For example, if we have 3 items, we will have 8 possible combinations of items
    # 000, 001, 010, 011, 100, 101, 110, 111 ...
    # 000 means that we don't take any item
    # 001 means that we take the first item
    # 010 means that we take the second item
    # 011 means that we take the first and second items
    # etc...
    for i in range(2**len(items)):
        combinaisons.append([])
        for j in range(len(items)):
            if (i >> j) % 2 == 1:
                combinaisons[i].append(items[j])

    # Here we check if the combinations of items fit in the knapsack
    # If they fit, we add them to the list of possible combinations
    for combinaison in combinaisons:
        poids = 0
        for item in combinaison:
            poids += item.weight
        if poids <= capacity:
            combinaisonsPossibles.append(combinaison)

    # Here we check which combination of items has the highest value
    # If they have the same value, we add them to the list of possible combinations with the highest value
    # If they have a higher value, we empty the list of possible combinations with the highest value and we add the new combination
    # If they have a lower value, we do nothing
    # We also update the highest value
    # We also update the list of items that make up the highest value combination
    for combinaison in combinaisonsPossibles:
        valeur = 0
        for item in combinaison:
            valeur += item.value
        if valeur > valeurMax:
            valeurMax = valeur
            combinaisonsPossiblesMax = [combinaison]
        elif valeur == valeurMax:
            combinaisonsPossiblesMax.append(combinaison)

    # Calculate the time of execution
    end_time = time.time()
    execution_time = end_time - start_time

    # Return the list of items that are in the knapsack and the time of execution
    return combinaisonsPossiblesMax, execution_time


###########################################################
############### MULTIDIMENSIONAL KNAPSACK #################
###########################################################

# This function is used to brute force the Multidimensional Knapsack problem
# It takes the list of itemMD, the list of capacities of the knapsacks and the number of knapsacks as parameters
# It give in output the best value, the list of items that can fit in all the dimensions of the knapsack and the time of execution
# It returns an empty list if no solution is found
# Its complexity is O(2^n)
# So it means that if we have 10 items, it will take 1024 operations to find the solution
# If we have 20 items, it will take 1,048,576 operations to find the solution
# If we have 30 items, it will take 1,073,741,824 operations to find the solution
# So it is very slow
# I think it is not recommended to use it with more than 20 items, but it always gives the optimal solution
def bruteForceMD(itemMD, capacities, nbrDimensions):

    # Calculate the time of execution
    start_time = time.time()

    # Create a list of all possible combinations of items
    combinaisons = []

    # Create a list of all possible combinations of items that fit in the knapsack
    combinaisonsPossibles = []

    # Create a list of all possible combinations of items that fit in the knapsack and that have the highest value
    combinaisonsPossiblesMax = []

    # We initialize the highest combination value to 0
    valeurMax = 0

    # We know that all possible combinations of items are 2^n
    # We create a list of all possible combinations of items
    # We use the binary system to create all possible combinations of items
    # For example, if we have 3 items, we will have 8 possible combinations of items
    # 000, 001, 010, 011, 100, 101, 110, 111 ...
    # 000 means that we don't take any item
    # 001 means that we take the first item
    # 010 means that we take the second item
    # 011 means that we take the first and second items
    # etc...
    for i in range(2**len(itemMD)):
        combinaisons.append([])
        for j in range(len(itemMD)):
            if (i >> j) % 2 == 1:
                combinaisons[i].append(itemMD[j])

    # Here we check if the combinations of items fit with all the dimensions of the knapsack
    # If they fit, we add them to the list of possible combinations
    for combinaison in combinaisons:
        poids = [0] * nbrDimensions
        for item in combinaison:
            for i in range(nbrDimensions):
                poids[i] += item.weight[i]
        if poids <= capacities:
            combinaisonsPossibles.append(combinaison)

    # Here we check which combination of items has the highest value
    # If they have the same value, we add them to the list of possible combinations with the highest value
    # If they have a higher value, we empty the list of possible combinations with the highest value and we add the new combination
    # If they have a lower value, we do nothing
    # We also update the highest value
    # We also update the list of items that make up the highest value combination
    for combinaison in combinaisonsPossibles:
        valeur = 0
        for item in combinaison:
            valeur += item.value
        if valeur > valeurMax:
            valeurMax = valeur
            combinaisonsPossiblesMax = [combinaison]
        elif valeur == valeurMax:
            combinaisonsPossiblesMax.append(combinaison)

    # Calculate the time of execution
    end_time = time.time()
    execution_time = end_time - start_time

    # Return the list of items that are in the knapsack, the time of execution and the best value
    return combinaisonsPossiblesMax, execution_time, valeurMax


def main(type, path):

    ##############################################################
    ############### EXECUTION OF SIMPLE KNAPSACK #################
    ##############################################################

    if (type == "simple"):

        # Here we create the items that we will use in the knapsack problem and we add them to a list of items, the path of the file is the parameter of the program
        nbrItems, capacity, items = ressources.readFileCreateList(path)

        # Here we call the brute force function and we get the list of possible combinations of items with the highest value
        sortedList, timeExec = bruteForce(capacity, items)

        # Here we initialize the highest value and the highest weight to 0
        finalValue = 0
        finalWeight = 0
        maxValue = 0

        # Here we print the list of possible combinations of items with the highest value and the highest weight that they can carry, and of course, the execution time of the algorithm
        for combinaison in sortedList:
            print()
            print("*******************Best Combinaisons*******************")
            print()
            for item in combinaison:
                maxValue += item.value
                finalWeight += item.weight
                item.printItem()
            print("Total Value : " + str(finalValue))
            print("Total Weight : " + str(finalWeight))
            finalValue = maxValue
            maxValue = 0
            finalWeight = 0

        print()
        print("*******************Execution Time*******************")
        print()
        print("Execution time: ", timeExec, " seconds")

    ########################################################################
    ############### EXECUTION OF MULTIDIMENSIONAL KNAPSACK #################
    ########################################################################

    else:

        # For the multidimensional knapsack problem, we have to get the list of items and the number of dimensions of the knapsack
        listeItemMD, nbrItems, nbrDimension, listeWeightKnapsack, optValue = ressources.readMultiDimFile(
            path)

        # Here we call the brute force function and we get the list of possible combinations of items with the highest value
        sortedList, timeExec, finalValue = bruteForceMD(
            listeItemMD, listeWeightKnapsack, nbrDimension)

        # Here we initialize the highest weight to 0
        finalWeight = [0] * nbrDimension

        # Here we print the list of possible combinations of items with the highest value and the highest weight that they can carry, and of course, the execution time of the algorithm
        for combinaison in sortedList:
            print()
            print("*******************Best Combinaisons*******************")
            print()
            for item in combinaison:
                for i in range(nbrDimension):
                    finalWeight[i] += item.weight[i]
                item.printItem()
            print("Total Weight : " + str(finalWeight))
            finalWeight = [0] * nbrDimension

        print()
        print("*******************Execution Time*******************")
        print()
        print("Execution time: ", timeExec, " seconds")

        print()
        print("*******************Optimal Value*******************")
        print()
        print("Optimal value found: ", finalValue)

    return timeExec, finalValue , nbrItems
