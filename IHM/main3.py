# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 00:24:18 2022

@author: thoma
"""


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


import pygame
import sys

nb_sprite = 20
cell_size = 35
height = nb_sprite*cell_size
width = height+200

BLACK = (0, 0, 0)
GREY = (150, 150, 150)


def main():
    global screen 
    screen = pygame.display.set_mode((width, height))
    screen.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def drawGrid():
    for x in range(0, height, cell_size):
        for y in range(0, height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, GREY, rect, 1)
            
            
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
