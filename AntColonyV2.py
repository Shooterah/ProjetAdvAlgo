class proba:
    
    def __init__(self, liType, phero):
        # List of the strenght attractive value (Ratio, Value or Weight)
        self.liType = liType
        # Index of the list
        self.ind = []
        # List of next probability for each element
        self.p = liType
        # Lenght of the probability
        self.n = len(liType)
        # Total of value of list of probability
        self.tmp = sum(self.p)
        # List of pheromones trail
        self.liTrail = []

        for i in range(self.n):
            # Init index of each element
            self.ind.append(i)
            # List of pheromone for each element
            self.liTrail.append(phero)
            # Calculate the probability
            self.p[i] /= self.tmp

        
            
    # Update the probability with trail of pheromones   
    def update(self, trail, Sb):
        # Update the trail of pheromone list
        for i in Sb:
            self.liTrail[i] += trail
        # Init the new probability list
        self.p = []
        # Caclulate inital probability list
        for i in range(self.n):
            self.p.append(self.liTrail[i]*self.liType[i])
        # Calculate tmp
        self.tmp = sum(self.p)
        # Update the final probability list
        for i in range(self.n):
            self.p[i] /= self.tmp
            
    # Remove an element of the list
    def remove(self, i):
        self.liType.pop(i)
        self.p.pop(i)
        self.ind.pop(i)
        self.n -= 1
        self.update(0,[])
    
    # Action of evaporation
    def evaporate(self, ev):
        # Verification if ev is in [0-1]
        if(0 <= ev and ev < 1):
            for i in range(self.n):
                self.p[i] *= ev
                

            
        
        
    
        
x = [1,2,4,5]

P = proba(x,0.2)

print(P.p)
print(P.tmp)
print(P.ind)


P.update(0.5, [2,3])

print(P.p)
print(P.tmp)
print(P.ind)



P.remove(2)

print(P.p)
print(P.tmp)
print(P.ind)
