# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 00:24:18 2022

@author: thoma
"""


#Personnalisation de la fenêtre
image_planete="D:\GitHub\24h_code\ressources\planetes\planet-1.png"
titre_fenetre = "Space Travellers"
image_icone = "D:\GitHub\24h_code\ressources\icones\crewmate.png"
#image_fond = "ecran.png"

#Images des vaisseaux
droite="D:\GitHub\24h_code\ressources\spaceships\droite.png"
gauche="D:\GitHub\24h_code\ressources\spaceships\gauche.png"
haut="D:\GitHub\24h_code\ressources\spaceships\haut.png"
bas="D:\GitHub\24h_code\ressources\spaceships\bas.png"


import pygame
import sys

#from Strategy import RecupCoordPlanet


nb_sprite = 20
cell_size = 35
height = nb_sprite*cell_size
width = height+200
shipNumber=1
BLACK = (0, 0, 0)
GRID_COLOR = (87, 0, 113)


def main():
    global screen 
    screen = pygame.display.set_mode((width, height))
    zeecran=pygame.image.load("ecran3.png").convert_alpha()

    while True:
        screen.blit(zeecran, (0,0))
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #Rafraichissement
        pygame.display.flip()
        pygame.display.update()


def drawGrid():
    for x in range(0, height, cell_size):
        for y in range(0, height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)
            

#class map():
    
    #def generer(self,mapNumber):
        #print(RecupCoordPlanet(shipNumber,mapNumber))
        #structure_niveau = [RecupCoordPlanet(shipNumber,mapNumber)]
        
    
    
    
pygame.init()

#Icone
#icone = pygame.image.load(image_icone)
#pygame.display.set_icon(icone)

#Titre
pygame.display.set_caption(titre_fenetre)

main()
#map.generer(1)


