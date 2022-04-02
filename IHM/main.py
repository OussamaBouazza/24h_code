#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""
Created on Sat Apr  2 18:39:25 2022

@author: thomas
"""


#----------------Constantes----------------

BLACK = (0, 0, 0)
WHITE = (100, 100, 100)
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 900
global SCREEN, CLOCK


#Paramètres de la fenêtre
#nombre_sprite_cote = 15
#taille_sprite = 30
#cote_fenetre = nombre_sprite_cote * taille_sprite

#Personnalisation de la fenêtre
titre_fenetre = "Space Travellers"
#image_icone = ""

#Listes des images du jeu
#image_fond = "images/fond.jpg"

#----------------Classes-------------------

def drawGrid():
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    blockSize = 35 #Set the size of the grid block
    for x in range(0, 700, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)



#----------------Main--------------------

import pygame
import requests
import sys


pygame.init()


#Icone
#icone = pygame.image.load(image_icone)
#pygame.display.set_icon(icone)

#Titre
pygame.display.set_caption(titre_fenetre)



#BOUCLE PRINCIPALE
continuer = 1
while continuer:    
   #Création grille
   drawGrid()
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

   pygame.display.update()

   #Rafraichissement
   pygame.display.flip()

   #On remet ces variables à 1 à chaque tour de boucle
   continuer_jeu = 1
   continuer_accueil = 1

    
            
        

    

                
    
