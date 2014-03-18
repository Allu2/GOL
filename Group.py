__author__ = 'aleksi'
import Unit


class Group:
    def __init__(self, coords):
        self.indx = 0
        self.coords = coords
        self.creatures = []
        self.locations = set()

    def isUnit(self, x, y):
        self.getLocations()
        locations = self.locations
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
        lista.append([x[0] - 1, x[1]])
        lista.append([x[0] + 1, x[1]])
        lista.append([x[0] - 1, x[1] + 1])
        lista.append([x[0], x[1] + 1])
        lista.append([x[0] + 1, x[1] + 1])
        lista.append([x[0] + 1, x[1] - 1])
        lista.append([x[0], x[1] - 1])
        lista.append([x[0] - 1, x[1] - 1])
        return lista

    def getLocations(self):
        locations = []
        for i in self.getCreatures():
            locations.append(i.getPosition())
        self.locations = locations

    def createCreature(self, x, y):
        self.getLocations()
        if [x, y] in self.locations:
            pass
        else:
            self.creatures.append(Unit.Unit(x, y))

    def getCreatures(self):
        return self.creatures

    def setNeighs(self):
        lista = self.creatures
        locations = self.locations
        for i in lista:
            position = i.getPosition()
            possible_neighs = self.solveri(position)
            hits = 0
            for y in locations:
                for x in possible_neighs:
                    if y == x:
                        hits += 1
            i.setNeigh(hits)

    def hasNeigh(self, x, y):
        locations = self.locations
        position = [x, y]
        possible_neighs = self.solveri(position)
        hits = 0
        for y in possible_neighs:
            for x in locations:
                if y == x:
                    hits += 1
        return hits