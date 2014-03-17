__author__ = 'aleksi'
def display(size, unit_amount):
    marks = []
    ind = size
    for c in range(size):
        for y in range(size):
            if x.isUnit(c, y):
                marks.append("0 ")
            else:
                marks.append("* ")
        marks.append("\n")
    print(''.join(marks))

import Group, random, time, os
x = Group.Group()
size = 50
for i in range(size):
    randx = random.randrange(0,5)
    randy = random.randrange(0,5)
    x.createCreature(randx, randy)
x.setNeighs()
unit_amount = len(x.getCreatures())
#print("Point 3,3 has {} neighbours".format(x.hasNeigh(3,3)))
display(size, unit_amount)
indi = 10000
generation = 0
while indi > 0:
    start_t = time.time()
    x.setNeighs()
    q = 0
    lista = x.getCreatures()
    #print(lista)
    for i in lista:
        if i.neigh>3:
            x.creatures.remove(i)
        if i.neigh == 2 or i.neigh == 3:
            pass
        if i.neigh<2:
            x.creatures.remove(i)
    for i in range(size):
        for f in range(size):
            if not x.isUnit(i, f):
                neighs = x.hasNeigh(i, f)
                if neighs == 3:
                    x.createCreature(i, f)
    os.system('cls' if os.name == 'nt' else 'clear')
    display(size, unit_amount)
    end_t = time.time()
    total_t = end_t-start_t
    print("Generation {} \nTotal number of cells: {}\nTime spend calculating:{}".format(generation,len(x.getCreatures()), total_t))
    indi -= 1
    generation += 1
    time.sleep(0.01)

