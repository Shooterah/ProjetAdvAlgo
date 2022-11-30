from tkinter.messagebox import NO


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
        return str(" V: "+ str(self.value) + " W: "+ str(self.weight))


# A node is of a tree is composed of :

    # 1] an item called data.
    # 2] a level that allow us to know on each node at which depht it is.
    # 3] CumValue is used to stock the value of all item already selected in the node.
    # 4] CumWeight is also used to stock the value of the total weight of item already selected in the current node.
    # 5] MaxValue is used to stock the value of the bound of the node.
    # 5] and 6] the lef and right children who are the same but the left is used for a selected item and the right for an unselected one.

class Node:
    def __init__(self,data,CumValue, MaxValue,CumWeight,Left_children,Right_children,level):
        self.data = data
        self.level = level
        self.CumWeight = CumWeight
        self.CumValue = CumValue
        self.MaxValue = MaxValue
        self.Left_children = Left_children
        self.Right_children = Right_children

# This fonction help us to add node in our tree at the folowing of already placed nodes.
# We don't put data on leaf but we add the Cumulated Value  and the Cumulated Weight

    def addNode(self,newdata,CumValue,MaxValue,CumWeight,Left_children,Right_children,level):
        # If the node is empty we add the data
        if self.data == None:
            self.data = newdata
            self.level = level
            self.CumWeight = CumWeight
            self.CumValue = CumValue
            self.MaxValue = MaxValue
            self.Left_children = Left_children
            self.Right_children = Right_children
        # If the node is not empty we add the data in the left and right children
        else :
            # if the level = 2 we also add data in the left and right grandchildren
            if level == 2:
                self.Left_children = Node(newdata,CumValue+self.data.value,MaxValue,self.CumWeight+self.data.weight,Node(None,newdata.value+self.CumValue+self.data.value,MaxValue,newdata.weight+self.CumWeight+self.data.weight,None,None,level-2),Node(None,self.CumValue+self.data.value,MaxValue-self.data.value,self.CumWeight+self.data.weight,None,None,level-2),level-1)
                self.Right_children = Node(newdata,self.CumValue,MaxValue-self.data.value,self.CumWeight,Node(None,newdata.value+self.CumValue,MaxValue-self.data.value,newdata.weight+self.CumWeight,None,None,level-2),Node(None,self.CumValue,MaxValue-(self.data.value-newdata.value),self.CumWeight,None,None,level-2),level-1)
            # if the level > 2 we add data in the left and right children 
            else:
                #if the left children is empty we add the data in the left children
                if  self.Left_children is None:
                    self.Left_children = Node(newdata,CumValue+self.data.value,MaxValue,self.CumWeight+self.data.weight,None,None,level-1)
                else : 
                    #recursive call to add the data in the left children
                    self.Left_children.addNode(newdata,CumValue+self.data.value,MaxValue,self.CumWeight+self.data.weight,None,None,level-1)
                if self.Right_children is None:
                    # if the Right children is empty we add the data in the left children
                    self.Right_children = Node(newdata,self.CumValue,MaxValue-self.data.value,self.CumWeight,None,None,level-1)
                else :
                    #recursive call to add the data in the right children
                    self.Right_children.addNode(newdata,self.CumValue,MaxValue-self.data.value,self.CumWeight,None,None,level-1)

# Print the tree with a level distinction
    def printTree(self):
        i = 0
        tab = ""
        while i < self.level:
        # indent the node according to its level
            tab = tab+"\t"
            i+=1
        if self.data == None:
        # print the node if it is empty 
            print(tab+"Empty"+" L: "+str(self.level)+" CV: "+str(self.CumValue)+" CW: "+str(self.CumWeight))
        else:
        # print the node if it is not empty with the data and all the cumulated value and weight 
            print(str(tab)+"L:" +str(self.level)+str(item.printItemTree(self.data))+" CV: "+str(self.CumValue)+" CW: "+str(self.CumWeight) + " MV: " + str(self.MaxValue))
            if self.Left_children:
            # recursive call to print the left children
                self.Left_children.printTree()
            if self.Right_children:
            # recursive call to print the right children
                self.Right_children.printTree()

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
    
    
# Structure of an item for the multidimensional knapsack problem
# The item is composed of :
# 1] the value of the item
# 2] a list of weight for each dimension
# 3] a list of ratio for each dimension
# 4] a position in the list of item
class itemMD:
    def __init__(self,pos,value,weight, ratio):
        self.pos = pos # Position in the list of item
        self.value = value # Value of the item
        self.weight = weight # weight(vector) of the item for each dimension
        self.ratio = ratio # List of ratio for each dimension

    def printItem(self):
        print("-------------------------------------")
        print("| Pos : ", self.pos, "Value : ", self.value)
        for i in range(len(self.weight)):
            print("| Weight : ", self.weight[i], "Ratio : ", self.ratio[i], "Dimension : ", i)
    
    
# This function will create a list of item used for the multidiemensional knapsack problem by reading a dataset file.
# It take the path of the file as parameter
# It return the list if item, the weight of all dimension, and the optimal value of the problem.
def readMultiDimFile(path):
    #List of Items
    listItem = []
    #List of weight of each dimension
    weightDim = []
    # Nbr of item
    n = 0
    # Nbr of dimension
    d = 0
    # Optimal value
    opt = 0
    with open(path) as f:
        firstline = f.readline().rstrip()
        words = firstline.split(" ")
        n = int(words[0])
        d = int(words[1])
        opt = int(words[2])
        
        data = f.read()

        value = []
        weight = [[0 for x in range(d)] for y in range(n)]
        ratio = [[0 for x in range(d)] for y in range(n)]
        listeDonnee = []
        
        # Put the data into a list
        for line in data.split("\n"):
            for word in line.split(" "):
                listeDonnee.append(word)
        
        index = 0
        
        # Create the list of item value     
        for j in range(n):
            # Value of item i
            value.append(int(listeDonnee[index])) 
            index += 1
        
        # Create the list of item weight for each dimension
        for i in range(n):
            for j in range(d):
                # Weight of item i in dimension j
                weight[i][j] = int(listeDonnee[index])
                index += 1
            
        # Create the list of item ratio for each dimension
        for i in range(n):
            for j in range(d):
                # Ratio of item i in dimension j
                ratio[i][j] = value[i]/weight[i][j]
                
        # Create the list of item
        for i in range(n):
            listItem.append(itemMD(i,value[i],weight[i],ratio[i]))
            
        # Create the list of weight for each dimension
        for i in range(d):
            weightDim.append(int(listeDonnee[index]))
            index += 1
            
    return listItem, n, d, weightDim, opt



