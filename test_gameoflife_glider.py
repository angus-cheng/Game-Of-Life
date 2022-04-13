# -*- coding: utf-8 -*-
"""
Game of life script with animated evolution

Created on Tue Jan 15 12:37:52 2019

@author: shakes
"""
import conway

#N = 64
#N = 1025
N = 125

#create the game of life object
life = conway.GameOfLife(N)
#life.insertBlinker((0,0))
#life.insertGlider((0,0))
with open("./cordershipRake.txt", "r") as text_file:
        txtString = text_file.read()
with open("barge2Extend.rle", "r") as rle_file:
        rleString = rle_file.read()
#life.insertFromPlainText("./noahsArk.txt")
# life.insertFromPlainText(txtString)
life.insertFromRLE(rleString)
cells = life.getStates() #initial state

#-------------------------------
#plot cells
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

plt.gray()

img = plt.imshow(cells, animated=True)

def animate(i):
    """perform animation step"""
    global life
    
    life.evolve()
    cellsUpdated = life.getStates()
    
    img.set_array(cellsUpdated)
    
    return img,

interval = 250 #ms

#animate 24 frames with interval between them calling animate function at each frame
ani = animation.FuncAnimation(fig, animate, frames=24, interval=interval, blit=True)

plt.show()
text_file.close()