
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


# We create a function that will return a random solution, for the distribution we will use the ratio of the value of the item to the weight of the item. The function take in parameters the number of items, the weight of the knapsack, and the list of items. The function return the solution and the time to find the solution. (The ratio of the item is stocked in the variable item.ratio)
# For the best case, its complexity is O(n) because we have a loop that will run n times. And all items have the good criteria and can fit in the knapsack. So, we will have a solution with all items.
# For the worst case, its complexity is O(n*(n-1)) because we have a loop that will run n times and this loop can run n-1 times (with the decrementation of the criteria).
def randomSolution(capacity, items, nbrItems):

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

    #Shuffle the list of items to have a random selection
    random.shuffle(items)
    
    
    # We create a loop that will select the items that have a ratio higher or equal to the criteria and that can fit in the knapsack ans stock them in the solution list.
    # We stop the loop if:
    # We cannot add more items in the knapsack because of the weight, we break the loop.
    # The number of items in the solution is equal to the number of items, we break the loop.
    # If we cannot add more items in the knapsack because of the criteria, we will decrease the criteria by 1% and we will continue the loop.
    while True:
        for item in items:
            if item.ratio >= criteria and weightSolution(solution) + item.weight <= capacity:
                # We add the item in the solution
                solution.append(item)
                # We remove the item from the list of items
                items.remove(item)
            # If the weight of the solution is higher than the weight of the knapsack, or the number of items in the solution is equal to the number of items, we break the loop.
            if weightSolution(solution) >= capacity or len(solution) == nbrItems:
                break
        # If we cannot add more items in the knapsack because of the weight, we break the loop.
        nbrCannotAdd = 0
        for item in items:
            if weightSolution(solution) + item.weight > capacity:
                nbrCannotAdd += 1
        if nbrCannotAdd == len(items):
            break
        # We decrease the criteria by 1%
        criteria = criteria - (criteria * 0.01)
        
    # We calculate the time of execution of the algorithm
    end_time = time.time()
    execution_time = end_time - start_time

    # We return the solution and the time to find the solution
    return solution, execution_time




# We create a function that will return a random solution for the multiDimensional Knapsack Problem, for the distribution we will use the ratio of the value of the item to the weight of the item. The function take in parameters the number of items, the weight of the knapsack, and the list of items. The function return the solution and the time to find the solution. (The ratio of the item is stocked in the variable item.ratio)
# For the best case, its complexity is O(nm) because we have a loop that will run n times (nbr items) and a loop that will run m times (nbr dimensions). And all items have the good criteria and can fit in the knapsack. So, we will have a solution with all items.
def randomSolutionMultiDimensional(capacity, items, nbrItems, nbrDimensions):

    # We calculate the time of execution of the algorithm
    start_time = time.time()
    
    # We create a list that will contain the solution
    solution = []

    # We create the criteria for the random selection, we will take the average of the ratio of the items in the list of items and we will add 1% of this average to the criteria. We will use this criteria to select the items. We will select the items that have a ratio higher than the criteria. We will do this until the weight of the solution is higher than the weight of the knapsack. We will also stop the loop if the number of items in the solution is equal to the number of items.
    # We do this for all dimensions.
    
    criteria = [0 for i in range(nbrDimensions)]
    for item in items:
        for i in range(nbrDimensions):
            criteria[i] += item.ratio[i]
    for i in range(nbrDimensions):
        criteria[i] = criteria[i] / len(items)
        criteria[i] = criteria[i] + (criteria[i] * 0.01)

    #Shuffle the list of items to have a random selection
    random.shuffle(items)
    
    
    # We create a loop that will select the items that have a ratio higher or equal to the criteria and that can fit in all dimensions of the knapsack ans stock them in the solution list.
    # We stop the loop if:
    # We cannot add more items in the knapsack because of the dimensions, we break the loop.
    # The number of items in the solution is equal to the number of items, we break the loop.
    # If we cannot add more items in the knapsack because of the criteria, we will decrease the criteria by 1% and we will continue the loop.
    while True:
        for item in items:
            # Check if the ratio of the item is higher or equals than the criteria
            # Check if the item can fit in all dimensions of the knapsack (With the array of the weight of the item and the array of the weight of the knapsack and the array of the weight of the solution)
            if ratioHigherOrEqualsThanCriteria(item.ratio, criteria) and canFitInAllDimensions(item.weight, capacity, weightSolutionMultiDimensional(solution, nbrDimensions)):
                # We add the item in the solution
                solution.append(item)
                # We remove the item from the list of items
                items.remove(item)                
            # If the weight of the solution is higher than the weight of the knapsack, or the number of items in the solution is equal to the number of items, we break the loop.
            if weightSolutionMultiDimensional(solution, nbrDimensions) >= capacity or len(solution) == nbrItems:
                break
        # If we cannot add more items in the knapsack because of the weight, we break the loop.
        nbrCannotAdd = 0
        for item in items:
            if canFitInAllDimensions(item.weight, capacity, weightSolutionMultiDimensional(solution, nbrDimensions)) == False:
                nbrCannotAdd += 1
        if nbrCannotAdd == len(items):
            break
        # We decrease all the criteria by 1%
        for i in range(nbrDimensions):
            criteria[i] = criteria[i] - (criteria[i] * 0.01)

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

# Function that return the weight of the solution for the multiDimensional Knapsack Problem. The list of items is stocked in the solution. The weight of each dimension of each item is stocked in the variable item.weight. The function take in parameters the solution. The function return the weight of the solution for each dimension.
def weightSolutionMultiDimensional(solution, nbrDimensions):
    # We create a list that will contain the weight of the solution for each dimension
    weight = [0 for i in range(nbrDimensions)]
    # We create a loop that will calculate the weight of the solution for each dimension
    for item in solution:
        for i in range(nbrDimensions):
            weight[i] += item.weight[i]
    # We return the weight of the solution for each dimension
    return weight

# Function that says if an Multidimensional Item can fit in all the dimension of the knapsack. The function take in parameters the weights of the item, the weights of the knapsack, and the weights of the solution. The function return True if the item can fit in all dimensions of the knapsack, and False if the item cannot fit in all dimensions of the knapsack.
def canFitInAllDimensions(itemWeight, knapsackWeight, solutionWeight):
    # We create a loop that will check if the item can fit in all dimensions of the knapsack
    for i in range(len(itemWeight)):
        if itemWeight[i] + solutionWeight[i] > knapsackWeight[i]:
            return False
    # If the item can fit in all dimensions of the knapsack, we return True
    return True

# Function that says if all the ratio of the item are higher or equals than the criterias. The function take in parameters the ratio of the item and the criteria. The function return True if all the ratio of the item are higher or equals than the criterias, and False if not.
def ratioHigherOrEqualsThanCriteria(itemRatio, criteria):
    # We create a loop that will check if all the ratio of the item are higher or equals than the criterias
    for i in range(len(itemRatio)):
        if itemRatio[i] < criteria[i]:
            return False
    # If all the ratio of the item are higher or equals than the criterias, we return True
    return True


def main(type, path):
    
    if(type == "simple"):
        
        # Execution of the random approach for the simple knapsack problem
        
        # We stock the number of item, the weight of the knapsack, and the list of item in the variable n, wmax, and listItem respectively. We use the function readFileCreateList from the ressources.py file.
        nbrItems, capacity, items = ressources.readFileCreateList(path)

        # We test the algorithm
        solution, execution_time = randomSolution(capacity, items, nbrItems)

        for item in solution:
            item.printItem()
        print("Value of the solution: ", valueSolution(solution))
        print("Weight of the solution: ", weightSolution(solution))
        print("Execution time: ", execution_time)
        
        return execution_time, valueSolution(solution)
    
    elif(type == "multiDim"):
        
        # Execution of the random approach for the multi-dimensional knapsack problem
        items, nbrItems, nbrDimensions, capacity, optValue = ressources.readMultiDimFile(path)
        
        # We test the algorithm
        solution, execution_time = randomSolutionMultiDimensional(capacity, items, nbrItems, nbrDimensions)

        for item in solution:
            item.printItem()
        print("Value of the solution: ", valueSolution(solution))
        print("Weight of the solution: ", weightSolutionMultiDimensional(solution, nbrDimensions))
        print("Execution time: ", execution_time)

        return execution_time, valueSolution(solution)