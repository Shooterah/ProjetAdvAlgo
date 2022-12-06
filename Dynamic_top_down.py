# Made by Arthur Micol
import time
import ressources

# for add knapsack constitution , add a table where it's stock the value of the knapsack for each branch
finalknapsack = []


class memo:
    def __init__(self, Remain_weight, nb_rem_items, max_value):
        self.Remain_weight = Remain_weight
        self.nb_rem_items = nb_rem_items
        self.max_value = max_value


# tree found on https://pixees.fr/informatiquelycee/n_site/nsi_term_projet_4.html

def dynamic_tree(items, capacity, nb_items):
    tabmemo = []
    return dynamic_tree_rec(items, capacity, nb_items, tabmemo)


def dynamic_tree_rec(items, capacity, nb_items, tabmemo):
    # print("nb_items : ", nb_items, "capacity : ", capacity)

    # if the knapsack is full (in term of weight or if there is no more items)
    if capacity == 0 or nb_items == 0:
        return 0

    # let's check if we already make this sub-tree (compare remaining weight and nb of remaining items)
    for mem in tabmemo:
        if mem.Remain_weight == capacity and mem.nb_rem_items == nb_items:
            # print("a")
            return mem.max_value

    # if we don't have this sub-tree, we create it
    # we check if the last item is too heavy
    if items[nb_items - 1].weight <= capacity:
        # we check if we take the last item or not
        with_last_item = items[nb_items - 1].value + dynamic_tree_rec(items, capacity - items[nb_items - 1].weight,
                                                                      nb_items - 1, tabmemo)
        without_last_item = dynamic_tree_rec(
            items, capacity, nb_items - 1, tabmemo)

        # we check which one is the best
        if with_last_item > without_last_item:
            # print("b")
            tabmemo.append(memo(capacity, nb_items, with_last_item))
            return with_last_item
        else:
            # print("c")
            tabmemo.append(memo(capacity, nb_items, without_last_item))
            return without_last_item
    else:
        # print("d")
        tabmemo.append(memo(capacity, nb_items, dynamic_tree_rec(
            items, capacity, nb_items - 1, tabmemo)))
        # we don't take the last item
        return dynamic_tree_rec(items, capacity, nb_items - 1, tabmemo)

####################MAIN####################

def main(type, path):
    # Here we create the items that we will use in the knapsack problem and we add them to a list of items
    if type == "simple":
        nbrItems, capacity, items = ressources.readFileCreateList(path)
        # "Data/low-dimensional/test_arthur.txt")

        # add condition if capacity is 0

        # some print
        # print("\n Nbr of items : ", nbrItems)
        # print("\n Capacity : ", capacity)

        # list of items (0 to n-1)
        # print("\n List of items : ")
        # for i in items:
        #     print(i.printItem())
        
        start = time.time()
        # without tree
        MaxValue = dynamic_tree(items, capacity, nbrItems)
        start = time.time() - start
        # # green in terminal
        # print('\033[92m')
        # print("\n Max value : ", MaxValue)
        # # standar color in terminal
        # print('\033[0m')
    if type == "multi":
        MaxValue = 0
        start = 0
    return start, MaxValue , nbrItems

