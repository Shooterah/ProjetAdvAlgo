import ressources

# This function is used to resolve the Knapsack problem with the branch and bound method

nbrItems, capacity, items = ressources.readFileCreateList("Data/low-dimensional/f3_l-d_kp_4_20.txt")

Tree = ressources.Node(None)
for data in items:
    ressources.Node.addNode(Tree,data)

ressources.Node.display(Tree)