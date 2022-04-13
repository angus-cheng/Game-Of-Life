import conway

N = 64

gosperGlideGun = "./gosperGliderGun.txt"
noahsArk = "./noahsArk.txt"
test = "./test.txt"
with open(gosperGlideGun, "r") as text_file:
        txtString = text_file.read()

#create the game of life object
life = conway.GameOfLife(N)
life.insertFromPlainText(txtString, 5)
cells = life.getStates() #initial state

#evolve once
life.evolve()
cellsUpdated1 = life.getStates()

#evolve twice
# life.evolve()
# cellsUpdated2 = life.getStates()

#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import numpy as np

plt.figure(0)
plt.gray()
plt.imshow(cells)

ax = plt.gca()
# Minor ticks
ax.set_xticks(np.arange(-.5, N, 1), minor=True);
ax.set_yticks(np.arange(-.5, N, 1), minor=True);
#grid
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)

plt.figure(1)
ax = plt.figure(1)
ax = plt.gca()
ax.set_xticks(np.arange(-.5, N, 1), minor=True);
ax.set_yticks(np.arange(-.5, N, 1), minor=True);
ax.grid(which='minor', color='w', linestyle='-', linewidth=1)
plt.imshow(cellsUpdated1)

# plt.figure(2)
# ax = plt.figure(2)
# ax = plt.gca()
# ax.set_xticks(np.arange(-.5, N, 1), minor=True);
# ax.set_yticks(np.arange(-.5, N, 1), minor=True);
# ax.grid(which='minor', color='w', linestyle='-', linewidth=1)
# plt.imshow(cellsUpdated2)

plt.show()
text_file.close()