import conway

#N = 64
N = 150

gosperGlider = "./gosperGliderGunRLE.rle"
barge2 = "./barge2Extend.rle"

with open(barge2, "r") as rle_file:
        rleString = rle_file.read()

#create the game of life object
life = conway.GameOfLife(N)
life.insertFromRLE(rleString, 5)
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
