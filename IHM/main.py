#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""
Created on Sat Apr  2 18:39:25 2022

@author: thomas
"""


import pygame
import requests
import sys

from classes import *
from constantes import *

global SCREEN, CLOCK
pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)

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

    
            
        

    

                
    
