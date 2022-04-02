# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:05:22 2022



@author: thomas
"""

import pygame
import sys
import requests


from constantes import *



    


def drawGrid():
    blockSize = 35 #Set the size of the grid block
    for x in range(0, 700, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
            
