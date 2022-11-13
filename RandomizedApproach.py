
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
