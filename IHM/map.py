# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:05:22 2022



@author: thoma
"""

import pygame
import sys
import requests


BLACK = (0, 0, 0)
WHITE = (100, 100, 100)
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 800


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    blockSize = 35 #Set the size of the grid block
    for x in range(0, 700, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
            
main()