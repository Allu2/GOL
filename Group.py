__author__ = 'aleksi'
import Unit
class Group:
    def __init__(self):
        self.indx = 0
        self.creatures = []
    def isUnit(self, x, y):
        locations = self.getLocations()
        #print(locations)
        query = [x, y]
        #print(query)
        if query in locations:
            return True
        else:
            return False
    def solveri(self, x):
        # 0,0  1,0  2,0,  0,1  1,2  2,0  2,1  2,2
        lista = []
        lista.append([x[0]-1, x[1]])
        lista.append([x[0]+1, x[1]])
        lista.append([x[0]-1, x[1]+1])
        lista.append([x[0], x[1]+1])
        lista.append([x[0]+1, x[1]+1])
        lista.append([x[0]+1, x[1]-1])
        lista.append([x[0], x[1]-1])
        lista.append([x[0]-1, x[1]-1])
        return lista
    def getLocations(self):
        locations = []
        for i in self.getCreatures():
            locations.append(i.getPosition())
        return locations
    def createCreature(self, x, y):
        locations = self.getLocations()
        lista = self.getCreatures()
        if [x, y] in locations:
            pass
        else:
            self.creatures.append(Unit.Unit(x, y))
    def getCreatures(self):
        return self.creatures
    def setNeighs(self):
        lista = self.getCreatures()
        locations = self.getLocations()
        #print(locations)
        for i in lista:
            position = i.getPosition()
            possible_neighs = self.solveri(position)
            #print("Position1:{}".format(position))
            #print("Possible Neighbours:{}".format(possible_neighs))
            #print("Neighs")
            #print(neighs)
            #print("Units:{}".format(locations))
            hits = 0
            for y in locations:
                for x in  possible_neighs:
                    if y == x:
                        hits = hits+1
            #hits = list(set(locations[0]).intersection(possible_neighs[0]))
            #print("Hits:{}".format(hits))
            #print(hits)
            i.setNeigh(hits)

        #for i in lista:
            #print(i)
            #print("This unit has: "+str(i.neigh)+" neighbours.")
    def hasNeigh(self, x,y):
        locations = self.getLocations()
        #print(locations)
        position = [x, y]
        possible_neighs = self.solveri(position)
        hits = 0
        for y in possible_neighs:
            for x in  locations:
                if y == x:
                    hits = hits+1
        return hits