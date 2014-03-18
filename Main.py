__author__ = 'aleksi'
def display(size):
    os.system('cls' if os.name == 'nt' else 'clear')
#    print(coordinates)
    marks = []
    ind = size

    for c in coordinates:
        if x.isUnit(c[0], c[1]):
            marks.append("0 ")
        else:
            marks.append("- ")

        if c[1] == size-1:
            marks.append("\n")
    print(''.join(marks))

import Group, random, time, os
from itertools import product


size = 35
coordinates = list(product(xrange(size), xrange(size)))
x = Group.Group(coordinates)
for i in range(size):
    randx = random.randrange(0,5)
    randy = random.randrange(0,5)
    x.createCreature(randx, randy)
for i in range(size):
    randx = random.randrange(30,35)
    randy = random.randrange(30,35)
    x.createCreature(randx, randy)
#x.createCreature(4,4)
#x.createCreature(4,5)
#x.createCreature(4,6)
#x.setNeighs()
unit_amount = len(x.creatures)
#print("Point 3,3 has {} neighbours".format(x.hasNeigh(3,3)))
display(size)
indi = 10000
generation = 0

for indi in range(10000):
    remove = []
    create = []
    start_t = time.time()
    #x.setNeighs()
    #q = 0

    #print(lista)
    #print(len(x.creatures))
    for i in coordinates:
        if not x.isUnit(i[0], i[1]):
            neighs = x.hasNeigh(i[0], i[1])
            if neighs == 3:
                create.append([i[0], i[1]])
        else:
            neighs = x.hasNeigh(i[0], i[1])
            lista = x.creatures
            for w in lista:
                if w.getPosition() == [i[0], i[1]]:
                    if neighs>3:
                        remove.append(w)
                    if neighs<2:
                        remove.append(w)
                    if neighs == 2 or neighs == 3:
                        pass
    for i in create:
        x.createCreature(i[0], i[1])
    for i in remove:
        x.creatures.remove(i)
    time.sleep(0.3)
    display(size)
    indi -= 1
    generation += 1
    end_t = time.time()
    print("Generation: {} \nTotal number of cells: {}\nCells in beginning: {}\nTime spend calculating: {}".format(generation,len(x.creatures), unit_amount, end_t-start_t))


