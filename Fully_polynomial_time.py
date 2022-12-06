import ressources
import time


def fullpoly(items, capacity, nb_items):
    print("Full polynomial time")
# Dynamic is efficient if the value of items are small , that allow to have bigger values


def main(type, path):
    nbrItems = 0
    capacity = 0
    best_Value =0
    items = []

    if type == "simple":
        nbrItems, capacity, items = ressources.readFileCreateList(path)
        start = time.time()
        fullpoly(items, capacity, nbrItems)
        start = time.time() - start
    if type == "multi":
        best_Value = 0
        start = 0
    return start, best_Value, nbrItems