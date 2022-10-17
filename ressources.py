class item:
    def __init__(self, pos, value, weight):
        self.pos = int(pos)
        self.value = float(value)
        self.weight = float(weight)
        self.ratio = float(value) / weight

    def printItem(self):
        #print("Value : " + str(self.value) + "| Weight : " + str(self.weight) + "Ratio : " + str(self.ratio) + " InitPos : " + str(self.pos))
        print("|  Value : %-8.2f |\t Weight : %-8.2f |\tRatio : %-8.4f |\tInitPos : %-6d |" % (self.value,self.weight,self.ratio ,self.pos))

    def printItemTree(self):
        return str("V"+ str(self.value) + " W"+ str(self.weight))

class Node:
    def __init__(self,data):
        self.data = data
        self.Right_children = None
        self.Left_children = None

    def addNode(self,newdata):
        if self.data == None:
            self.data = newdata
        else :
            if self.Right_children is None:
                self.Right_children = Node(newdata)
            else : self.Right_children.addNode(newdata)
            if  self.Left_children is None:
                self.Left_children = Node(newdata)
            else : self.Left_children.addNode(newdata)

    def printTree(self):
        item.printItem(self.data)
        if self.data == None:
            print("Empty")
        else:
            if self.Left_children:
                self.Left_children.printTree()
            if self.Right_children:
                self.Right_children.printTree()

    
    #juste pour plus visible lors des test supprimer lors du rendu final

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""    
        # No child.
        if self.Right_children is None and self.Left_children is None:
            line = '%s' %  item.printItemTree(self.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Two children.
        left, n, p, x = self.Left_children._display_aux()
        right, m, q, y = self.Right_children._display_aux()
        s = '%s' % item.printItemTree(self.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


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
        i = 2
        for line in f:
            data = line.split(" ")
            listItem.append(item(i,float(data[0]), float(data[1])))
            i += 1
    return n, wmax, listItem

def fullLine(n):
    for i in range(n):
        print("-",end="")
    print("\b")