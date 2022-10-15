import ressources


def bruteForce(capacity, items):
    
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
    return combinaisonsPossiblesMax


# Here we create the items that we will use in the knapsack problem and we add them to a list of items
nbrItems, capacity, items = ressources.readFileCreateList("Data/low-dimensional/f10_l-d_kp_20_879.txt")

# Here we call the brute force function and we get the list of possible combinations of items with the highest value
sortedList = bruteForce(capacity, items)

# # Here we initialize the highest value and the highest weight to 0
finalValue = 0
finalWeight = 0

# Here we print the list of possible combinations of items with the highest value and the highest weight that they can carry
for combinaison in sortedList:
    print("*******************Best Combinaisons*******************")
    for item in combinaison:
        finalValue += item.value
        finalWeight += item.weight
        item.printItem()
    print("Total Value : " + str(finalValue))
    print("Total Weight : " + str(finalWeight))
    finalValue = 0
    finalWeight = 0