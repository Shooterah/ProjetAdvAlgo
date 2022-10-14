class item:
    def __init__(self, value, weight):
        self.value = float(value)
        self.weight = float(weight)
        self.ratio = float(value) / weight

    def printItem(self):
        print("Value : " + str(self.value) + " | Weight : " + str(self.weight) + " Ratio : " + str(self.ratio))


def readFileCreateList(path):
    #List of Items
    listItem = []
    # Nbr of item
    n = 0
    # Weight max of the bag
    wmax = 0
    with open(path) as f:
        firstline = f.readline().rstrip()
        words = firstline.split(" ")
        n = int(words[0])
        wmax = int(words[1])
        for line in f:
            data = line.split(" ")
            listItem.append(item(float(data[0]), float(data[1])))
    return n, wmax, listItem
