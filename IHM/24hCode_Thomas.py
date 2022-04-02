#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""
from pygame.locals import*
from time import *
import pygame
from pygame.locals import *

pygame.init()
font = pygame.font.Font(None, 90)
white = (255, 255, 255)



#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((1000, 700))

#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

#Titre
pygame.display.set_caption(titre_fenetre)


#BOUCLE PRINCIPALE
continuer = 1
while continuer:    
    #Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))

    #Rafraichissement
    pygame.display.flip()

    #On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    
            
        

    

                
    
