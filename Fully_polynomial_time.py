import ressources
import time
import Dynamic
from math import ceil
import numpy as np


def fullpoly(items, capacity, nb_items):
    print("Full polynomial time")
# Dynamic is efficient if the value of items are small , that allow to have bigger values
# trade off between the quality of the solution and the time
#epsilon > 0
# output is at least 1 - epsilon times the correct value, and at the most 1 + epsilon times the correct value
# Importantly, the run-time of an FPTAS is polynomial in the problem size and in 1/ε. This is in contrast to a general polynomial-time approximation scheme (PTAS). The run-time of a general PTAS is polynomial in the problem size for each specific ε, but might be exponential in 1/ε
    Valmax = 0
    epsilon = 0.1  # how good the approximation should be
    for item in items:
        if item.value > Valmax:
            Valmax = item.value

    thetas = (epsilon * Valmax) / nb_items  # scalling factor

    print("Valmax =", Valmax)
    print("thetas =", thetas)

    for item in items:
        item.value = ceil(item.value / thetas) * thetas
        print(item.value)

    # create the table of results and initialize it with 0 (capcity +1 because we start from 0)
    resTable = np.zeros((nb_items, capacity+1))
    # fill the table with the dynamic function
    a = Dynamic.DynamicInitTable(items, capacity+1, nb_items, resTable)

    # avoir le knapsack
    knapsack = []
    finalKnapsack = Dynamic.DynamicSearchSolution(
        a, int(capacity), nb_items-1, knapsack, items)
    MaxValue = a[nb_items-1, capacity]

    return MaxValue


def main(type, path):
    nbrItems = 0
    capacity = 0
    best_Value = 0
    items = []

    if type == "simple":
        nbrItems, capacity, items = ressources.readFileCreateList(path)
        start = time.time()
        best_Value = fullpoly(items, capacity, nbrItems)
        start = time.time() - start
    if type == "multi":
        best_Value = 0
        start = 0
    return start, best_Value, nbrItems
