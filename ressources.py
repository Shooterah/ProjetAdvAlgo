class item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
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
            listItem.append(item(int(data[0]), int(data[1])))
    return n, wmax, listItem
