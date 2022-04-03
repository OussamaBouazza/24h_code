# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 00:24:18 2022

@author: thoma
"""


#Personnalisation de la fenêtre
image_planete="\ressources\planetes\planet-1.png"
titre_fenetre = "Space Travellers"
image_icone = "\ressources\icones\crewmate.png"
#image_fond = "ecran.png"

#Images des vaisseaux
droite="\ressources\spaceships\droite.png"
gauche="\ressources\spaceships\gauche.png"
haut="\ressources\spaceships\haut.png"
bas="\ressources\spaceships\bas.png"


import pygame
import sys
#import commande
import time
#from Strategy import RecupCoordPlanet
#from Strategy import vaisseauFaitSaVie


nb_sprite = 20
cell_size = 35
height = nb_sprite*cell_size
width = height+200
shipNumber=1
mapNumber=2
BLACK = (0, 0, 0)
GRID_COLOR = (87, 0, 113)

#Texte



def main():
    
        map.generer(2,2) 


def drawGrid():
    for x in range(0, height, cell_size):
        for y in range(0, height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)
            

def generer(shipNumber,mapNumber, water):
        #vaisseauFaitSaVie(shipNumber, mapNumber)
        #blue = (0, 0, 128)
        #white = (255, 255, 255)
        global screen 
        screen = pygame.display.set_mode((width, height))
        zeecran=pygame.image.load("ecran.png").convert_alpha()
        white = (255, 255, 255)
        green = (0, 255, 0)
        blue = (0, 0, 128)
 
        X = 1700
        Y = 100

        
            
            
        
 
        
 
        pygame.display.set_caption('Show Text')
 
        font = pygame.font.Font('freesansbold.ttf', 10)
        
        text = font.render(str(water), True, green, blue)
 
        textRect = text.get_rect()
 
        textRect.center = (X // 2, Y // 2)
        
        
 
        
       
        screen.blit(zeecran, (0,0))
        drawGrid()
        screen.blit(text, textRect)
        #display_surface.fill(white)
        #display_surface.blit(texte, textRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #Rafraichissement
        pygame.display.flip()
        pygame.display.update()
        
        
        
        for event in pygame.event.get():
            pygame.display.update()
        time.sleep(1)
        
        
        #structure_niveau = [RecupCoordPlanet(shipNumber,mapNumber)]
    
  
pygame.init()

#Icone
icone = pygame.image.load("crewmate.png")
pygame.display.set_icon(icone)

#Titre
#vaisseauFaitSaVie(shipNumber, mapNumber)
#print(RecupCoordPlanet(shipNumber,mapNumber))

#main()






   
 