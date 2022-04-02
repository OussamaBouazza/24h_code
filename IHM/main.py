#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""
Created on Sat Apr  2 18:39:25 2022

@author: thomas
"""
#----------------Import--------------------
import pygame
import requests
import sys
from array import *
from pygame.math import Vector2
from pygame.draw import line
#----------------Constantes----------------


#Personnalisation de la fenêtre
image_planete="D:\GitHub\24h_code\ressources\planetes\planet-1.png"
titre_fenetre = "Space Travellers"
image_icone = "D:\GitHub\24h_code\ressources\icones\crewmate.png"
#image_fond = "images/fond.jpg"

#Images des vaisseaux
droite="D:\GitHub\24h_code\ressources\spaceships\droite.png"
gauche="D:\GitHub\24h_code\ressources\spaceships\gauche.png"
haut="D:\GitHub\24h_code\ressources\spaceships\haut.png"
bas="D:\GitHub\24h_code\ressources\spaceships\bas.png"


#Paramètres de la fenêtre

BLACK = (0, 0, 0)
WHITE = (100, 100, 100)
GREY = (50, 50, 50)


#----------------Classes-------------------

class Grille:
    nb_sprite = 20
    cell_size = 35
    x = 0
    y = 0
    height = nb_sprite*cell_size
    width = height+200
    center_cell = None
    color= (50, 50, 50)
    
    
    def __init__(self, x, y, width, height, cell_size):	
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.center_cell = Vector2((width - 1) / 2, (height - 1) / 2)
        
    def display1(self, screen):
        
        # Horizontal
        for y in range(0, self.height + self.cell_size, self.cell_size):
            line(screen, self.color, Vector2(self.x, y + self.y), Vector2(self.x + self.width, y + self.y))

		# Vertical
        for x in range(0, self.width + self.cell_size, self.cell_size):
            line(screen, self.color, Vector2(x + self.x, self.y), Vector2(x + self.x, self.y + self.height))
       
    """def display2(self):
        nb_sprite = 20
        cell_size = 35
        height = nb_sprite*cell_size
        width = height+200
        for x in range(0, width, cell_size):
            for y in range(0, height, cell_size):
                rect = pygame.Rect(x, y, cell_size, cell_size)
                pygame.draw.rect(screen, WHITE, rect, 1)"""
            

def main():
    global screen
    pygame.init()
    
    grille = Grille(0,0,Grille.width,Grille.height,Grille.cell_size)
    screen = pygame.display.set_mode((Grille.width, Grille.height))
    #BOUCLE PRINCIPALE
    continuer = 1
    while continuer:    
        #Création grille
        grille.display(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
#----------------Main--------------------



pygame.init()


#Icone
#icone = pygame.image.load(image_icone)
#pygame.display.set_icon(icone)

#Titre
pygame.display.set_caption(titre_fenetre)

main()

pygame.display.update()

#Rafraichissement
pygame.display.flip()

#On remet ces variables à 1 à chaque tour de boucle
continuer_jeu = 1
continuer_accueil = 1

    
            
        

    

                
    
