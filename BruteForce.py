import ressources


def bruteForce(capacity, items):
    
    # On initialise la liste des combinaisons possibles
    combinaisons = []
    
    # On initialise la liste des combinaisons possibles qui ont un poids inférieur à la capacité du sac
    combinaisonsPossibles = []
    
    # On initialise la liste des combinaisons possibles qui ont un poids inférieur à la capacité du sac et qui ont la plus grande valeur
    combinaisonsPossiblesMax = []
    
    # On initialise la valeur de la combinaison possibles qui a la plus grande valeur
    valeurMax = 0

    
    # On teste toutes les combinaisons possibles 
    for i in range(2**len(items)):
        combinaisons.append([])
        for j in range(len(items)):
            if (i >> j) % 2 == 1:
                combinaisons[i].append(items[j])
                
                                        
    # On teste toutes les combinaisons possibles qui ont un poids inférieur à la capacité du sac
    for combinaison in combinaisons:   
        poids = 0   
        for item in combinaison:
            poids += item.weight        
        if poids <= capacity:
            combinaisonsPossibles.append(combinaison)
            
            
    # On teste toutes les combinaisons possibles qui ont un poids inférieur à la capacité du sac et qui ont la plus grande valeur
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


# On teste la fonction bruteForce avec les données du fichier data.txt
nbrItems, capacity, items = ressources.readFileCreateList("Data/low-dimensional/f10_l-d_kp_20_879.txt")

sortedList = bruteForce(capacity, items)

finalValue = 0
finalWeight = 0

for combinaison in sortedList:
    print("*******************MEILLEURE COMBINAISON*******************")
    for item in combinaison:
        finalValue += item.value
        finalWeight += item.weight
        item.printItem()
    print("Total Value : " + str(finalValue))
    print("Total Weight : " + str(finalWeight))
    finalValue = 0
    finalWeight = 0