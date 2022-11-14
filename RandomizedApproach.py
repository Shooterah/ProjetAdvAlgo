
# Knapsack Problem: Randomized Approach (Python)
# Author: Florian Doffemont

# Goal: Find a solution to the knapsack problem using a randomized approach.

# What does "random" mean? It mean that we are randomly selecting items from the list of items. We are not using any algorithm to select the items. We are just randomly selecting items.

# But there are many distribution to generate from. How to choose the right one for our problem? Because we want to find the best solution, we need to select the distribution that will give us the best solution. 

# To choose the best distribution, we need to think of a useful criteria for the random selection. We can use the ratio of the value of the item to the weight of the item. The higher the ratio, the better the item. I think it is a good criteria to use because it avoid many problems. For example, if we use the value of the item as the criteria, we will have a problem if the value of the item is very high but the weight of the item is very very high too. In this case, the ratio will be very low so the item is not very good. So, we will select this item and we will have a bad solution.

# We will use the same data as the others algorithms.

# Import the necessary libraries
import random
import time
import ressources

# We stock the number of item, the weight of the knapsack, and the list of item in the variable n, wmax, and listItem respectively. We use the function readFileCreateList from the ressources.py file.
nbrItems, capacity, items = ressources.readFileCreateList("Data/low-dimensional/f8_l-d_kp_23_10000.txt")


# We create a function that will return a random solution, for the distribution we will use the ratio of the value of the item to the weight of the item. The function take in parameters the number of items, the weight of the knapsack, and the list of items. The function return the solution and the time to find the solution. (The ratio of the item is stocked in the variable item.ratio)
def randomSolution(nbrItems, capacity, items):

    # We calculate the time of execution of the algorithm
    start_time = time.time()
    
    # We create a list that will contain the solution
    solution = []

    # We create the criteria for the random selection, we will take the average of the ratio of the items in the list of items and we will add 1% of this average to the criteria. We will use this criteria to select the items. We will select the items that have a ratio higher than the criteria. We will do this until the weight of the solution is higher than the weight of the knapsack. We will also stop the loop if the number of items in the solution is equal to the number of items. 
    
    criteria = 0
    for item in items:
        criteria += item.ratio
    criteria = criteria / len(items)
    criteria = criteria + (criteria * 0.01)

    
    # We shuffle the list of items
    random.shuffle(items)
    
    # We create a loop that will select the items that have a ratio higher or equal to the criteria and that can fit in the knapsack ans stock them in the solution list.
    # We stop the loop if:
    # We cannot add more items in the knapsack because of the weight, we break the loop.
    # The number of items in the solution is equal to the number of items, we break the loop.
    # If we cannot add more items in the knapsack because of the criteria, we will decrease the criteria by 1% and we will continue the loop.
    while True:
        for item in items:
            if item.ratio >= criteria and weightSolution(solution) + item.weight <= capacity:
                solution.append(item)
                # We remove the item from the list of items
                items.remove(item)
            if weightSolution(solution) >= capacity or len(solution) == nbrItems:
                break
        if weightSolution(solution) >= capacity or len(solution) == nbrItems:
            break   
        nbrCannotAdd = 0
        for item in items:
            if weightSolution(solution) + item.weight > capacity:
                nbrCannotAdd += 1
        if nbrCannotAdd == len(items):
            break         
        criteria = criteria - (criteria * 0.01)
        
    # We calculate the time of execution of the algorithm
    end_time = time.time()
    execution_time = end_time - start_time

    # We return the solution and the time to find the solution
    return solution, execution_time

# We create a function that will return the value of the solution. The function take in parameters the solution. The function return the value of the solution.
def valueSolution(solution):
    # We create a variable that will contain the value of the solution
    value = 0
    # We create a loop that will calculate the value of the solution
    for item in solution:
        value += item.value
    # We return the value of the solution
    return value

# We create a function that will return the weight of the solution. The function take in parameters the solution. The function return the weight of the solution.
def weightSolution(solution):
    # We create a variable that will contain the weight of the solution
    weight = 0
    # We create a loop that will calculate the weight of the solution
    for item in solution:
        weight += item.weight
    # We return the weight of the solution
    return weight

# We test the algorithm
solution, execution_time = randomSolution(nbrItems, capacity, items)

for item in solution:
    item.printItem()
print("Value of the solution: ", valueSolution(solution))
print("Weight of the solution: ", weightSolution(solution))
print("Execution time: ", execution_time)

# We test the algorithm 100 times
#for i in range(100):
    #solution, execution_time = randomSolution(nbrItems, capacity, items)
    #print("Solution: ", solution)
    #print("Value of the solution: ", valueSolution(solution, items))
    #print("Weight of the solution: ", weightSolution(solution))
    #print("Execution time: ", execution_time)
        