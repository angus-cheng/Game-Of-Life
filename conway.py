# -*- coding: utf-8 -*-
"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

Created on Tue Jan 15 12:21:17 2019

@author: shakes
"""
import numpy as np
from scipy import signal
import rle

class GameOfLife:
    '''
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    '''
    def __init__(self, N=256, finite=False, fastMode=False):
        self.grid = np.zeros((N,N), np.int)
        rows, columns = self.grid.shape
        self.columns = rows
        self.rows = columns
        self.neighborhood = np.ones((3,3), np.int) # 8 connected kernel
        self.neighborhood[1,1] = 0 #do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        
    def getStates(self):
        '''
        Returns the current states of the cells
        '''
        return self.grid
    
    def getGrid(self):
        '''
        Same as getStates()
        '''
        return self.getStates()

    def getNeighbors(self, x, y):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                xEdge = (x+i+self.rows) % self.rows
                yEdge = (y+j+self.columns) % self.columns
                total += self.grid[xEdge][yEdge]
        total -= self.grid[x][y]
        return total
               
    def evolve(self):
        '''
        Given the current states of the cells, apply the GoL rules:
        - Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        '''
        #PART A & E CODE HERE
        # Part A
        # nextState = np.copy(self.grid)
        # for x in range(self.rows):
        #     for y in range(self.columns):
        #         cellState = self.grid[x][y]
        #         neighbors = self.getNeighbors(x, y)
        #         if cellState == 0 and neighbors == 3:
        #             nextState[x][y] = self.aliveValue
        #         elif cellState == 1 and (neighbors < 2 or neighbors > 3):
        #             nextState[x][y] = self.deadValue
        #         else:
        #             nextState[x][y] = cellState
        # self.grid = nextState 

        # Part E
        convolvedBoard = signal.convolve(self.grid, self.neighborhood, mode='same')
        nextState = (((self.grid == 1) & (convolvedBoard > 1) & 
                (convolvedBoard < 4)) | ((self.grid == 0) & 
                (convolvedBoard == 3))).astype(int)
        print(nextState)
        self.grid = nextState
    
    def insertBlinker(self, index=(0,0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        
    def insertGlider(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1]+1] = self.aliveValue
        self.grid[index[0]+1, index[1]+2] = self.aliveValue
        self.grid[index[0]+2, index[1]] = self.aliveValue
        self.grid[index[0]+2, index[1]+1] = self.aliveValue
        self.grid[index[0]+2, index[1]+2] = self.aliveValue
        
    def insertGliderGun(self, index=(0,0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0]+1, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+2, index[1]+23] = self.aliveValue
        self.grid[index[0]+2, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+3, index[1]+13] = self.aliveValue
        self.grid[index[0]+3, index[1]+14] = self.aliveValue
        self.grid[index[0]+3, index[1]+21] = self.aliveValue
        self.grid[index[0]+3, index[1]+22] = self.aliveValue
        self.grid[index[0]+3, index[1]+35] = self.aliveValue
        self.grid[index[0]+3, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+4, index[1]+12] = self.aliveValue
        self.grid[index[0]+4, index[1]+16] = self.aliveValue
        self.grid[index[0]+4, index[1]+21] = self.aliveValue
        self.grid[index[0]+4, index[1]+22] = self.aliveValue
        self.grid[index[0]+4, index[1]+35] = self.aliveValue
        self.grid[index[0]+4, index[1]+36] = self.aliveValue
        
        self.grid[index[0]+5, index[1]+1] = self.aliveValue
        self.grid[index[0]+5, index[1]+2] = self.aliveValue
        self.grid[index[0]+5, index[1]+11] = self.aliveValue
        self.grid[index[0]+5, index[1]+17] = self.aliveValue
        self.grid[index[0]+5, index[1]+21] = self.aliveValue
        self.grid[index[0]+5, index[1]+22] = self.aliveValue
        
        self.grid[index[0]+6, index[1]+1] = self.aliveValue
        self.grid[index[0]+6, index[1]+2] = self.aliveValue
        self.grid[index[0]+6, index[1]+11] = self.aliveValue
        self.grid[index[0]+6, index[1]+15] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue
        self.grid[index[0]+6, index[1]+17] = self.aliveValue
        self.grid[index[0]+6, index[1]+23] = self.aliveValue
        self.grid[index[0]+6, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+7, index[1]+11] = self.aliveValue
        self.grid[index[0]+7, index[1]+17] = self.aliveValue
        self.grid[index[0]+7, index[1]+25] = self.aliveValue
        
        self.grid[index[0]+8, index[1]+12] = self.aliveValue
        self.grid[index[0]+8, index[1]+16] = self.aliveValue
        
        self.grid[index[0]+9, index[1]+13] = self.aliveValue
        self.grid[index[0]+9, index[1]+14] = self.aliveValue

        # Missing alive cell at (18, 6)
        self.grid[index[0]+6, index[1]+18] = self.aliveValue
        
    def insertFromPlainText(self, txtString, pad=0):
        '''
        Assumes txtString contains the entire pattern as a human readable pattern without comments
        '''
        index = (0, 0)
        gridString = []
        y = 0
        txtArray = txtString.split('\n')
        gridString = [i for i in txtArray if '!' not in i]
        for row in gridString:
            x = 0
            if not row: 
                y += 1
                continue
            for column in row:
                if column == '.':
                    self.grid[index[0]+y+pad, index[1]+x+pad] = self.deadValue
                else:
                    self.grid[index[0]+y+pad, index[1]+x+pad] = self.aliveValue
                x += 1
            y += 1

    def insertFromRLE(self, rleString, pad=0):
        '''
        Given string loaded from RLE file, populate the game grid
        '''
        index = (0, 0)
        y = 0
        pattern = rle.RunLengthEncodedParser(rleString)
        for row in pattern.pattern_2d_array:
            x = 0
            if not row: 
                y += 1
                continue
            for column in row:
                if column == 'b':
                    self.grid[index[0]+y+pad, index[1]+x+pad] = self.deadValue
                else:
                    self.grid[index[0]+y+pad, index[1]+x+pad] = self.aliveValue
                x += 1
            y += 1
        