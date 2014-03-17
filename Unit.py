__author__ = 'aleksi'
class Unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neigh = 0
    def getPosition(self):
        return [self.x, self.y]
    def setPosition(self, x, y):
        self.x = x
        self.y = y
    def setNeigh(self, neighbours):
        self.neigh = neighbours